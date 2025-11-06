#!/bin/bash
echo "🚀 Limpando caches antigos do Buildozer e python-for-android..."

# Parar em qualquer erro
set -e

# Caminho base
BUILD_PATH="$HOME/.buildozer/android"

# Removendo caches antigos
rm -rf "$BUILD_PATH/packages/pyjnius"
rm -rf "$BUILD_PATH/platform/build-armeabi-v7a_arm64-v8a"
rm -rf "$BUILD_PATH/platform/python-for-android"

echo "🧹 Limpando build atual..."
buildozer android clean || true

# Corrigir requirements automaticamente
echo "📝 Garantindo que o buildozer.spec tenha o PyJNIus corrigido..."
if grep -q "requirements" buildozer.spec; then
    sed -i '/^requirements/d' buildozer.spec
fi

echo "requirements = python3==3.10.12, kivy==2.2.1, openpyxl, cython==0.29.36, https://github.com/Zen-CODE/pyjnius/archive/refs/heads/fix-long-type.zip" >> buildozer.spec

echo "✅ Configuração ajustada!"
echo "⚙️ Iniciando nova compilação com PyJNIus corrigido..."
buildozer android debug

