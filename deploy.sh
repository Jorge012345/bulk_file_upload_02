#!/bin/bash

set -e  # Si algo falla, detiene el script

echo "🔍 Verificando si existe package.json..."

if [ ! -f "package.json" ]; then
  echo "📦 Creando package.json..."
  npm init -y
fi

echo "📥 Instalando dependencias compatibles..."
npm install --save-dev \
  serverless@4.10.0 \
  serverless-python-requirements@6.1.0 \
  serverless-offline@14.4.0 \
  serverless-dotenv-plugin@6.0.0 \
  --legacy-peer-deps

echo "🚀 Desplegando a AWS con Serverless..."
npx serverless deploy

echo "✅ Despliegue completado con éxito."