# Use a lightweight Node.js image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the application code
COPY . .

# Expose the port your Express app runs on (must match server)
EXPOSE 3000

# Start the app
CMD ["node", "server.js"]
