# Usamos la imagen oficial de Node.js
FROM node:18

# Directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copiar package.json y realizar la instalación de dependencias
COPY package*.json ./
RUN npm install

# Copiar el resto de los archivos del proyecto
COPY . .

# Exponer el puerto en el que escuchará la app
EXPOSE 3000

# Comando para iniciar la app
CMD ["node", "app.js"]
