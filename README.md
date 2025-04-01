# Bulk File Upload
- Docker: No
- Arquitectura serverless: Yes
- CI/CD: Codepipeline

## Libraries for local test:
1. nvm install 23.5.0
2. npm install -g serverless@4.7.0
2. npm install --save-dev serverless-python-requirements
3. npm install --save-dev serverless-offline
4. npm install --save-dev serverless-dotenv-plugin --legacy-peer-deps

## Comando para verificar si tiene un plugin instalado:
- npm list "nombre del plugin"
## Ejecutar offline:
- serverless offline
## Este comando obtiene la configuración general de un API Gateway específico en AWS
aws apigateway get-rest-api --rest-api-id "ID DEL APIGATEWAY"

## Comando para verificar configuracion actual de API Gateway
aws apigateway get-stage --rest-api-id "ID DEL APIGATEWAY" --stage-name dev
aws apigateway get-stage --rest-api-id n39fargsbi --stage-name dev

## Comando para testing
python3 -m pytest testing/test_create_batch.py -s

