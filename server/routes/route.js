const routes=require('express').Router();
const controller=require("../controller/controller")

routes.route('/api/scrapping')
    .post(controller.create_scrapping);

routes.route('/api/summary')
    .post(controller.create_summary);

routes.route('/api/sentiment')
    .post(controller.create_sentiment);

routes.route('/api/entity')
    .get(controller.create_entities);

routes.route('/api/competitors')
    .post(controller.create_competitors);






module.exports=routes;
