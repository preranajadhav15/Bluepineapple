# 1. Use official Node.js image
FROM node:18

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy package.json and package-lock.json (if exists)
COPY package*.json ./

# 4. Install dependencies
RUN npm install

# 5. Copy the rest of the project files
COPY . .

# 6. Expose port 3000
EXPOSE 3000

# 7. Start the app
CMD ["node", "main.js"]
