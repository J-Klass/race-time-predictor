# BUILD REACT APP

FROM node:11 AS static-build
WORKDIR /app

# Install dependencies
COPY package.json yarn.lock ./
RUN yarn install

# Copy files
COPY public public/
COPY race_time_predictor/client race_time_predictor/client/
COPY .browserslistrc .env.production .eslintignore .eslintrc.yaml babel.config.js postcss.config.js vue.config.js ./

# Build React app
RUN yarn build


# RUN FLASK SERVER

FROM python:3.6
WORKDIR /app

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system

# Copy static files (will be served by nginx)
COPY --from=static-build /app/dist ./dist/

# Copy Flask app
COPY .env.production run.py ./
COPY race_time_predictor ./race_time_predictor/

# Run Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
