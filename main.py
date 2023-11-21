from cnnClassifier import logger


STAGE_NAME = "Data ingestion stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e