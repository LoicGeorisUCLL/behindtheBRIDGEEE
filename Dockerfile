FROM libretranslate/libretranslate:latest

# Set environment variables for Railway
ENV LT_DISABLE_WEB_UI=false
ENV LT_DEBUG=false
ENV LT_SSL=false
ENV LT_HOST=0.0.0.0
ENV LT_PORT=$PORT

# Expose the port (Railway will set $PORT automatically)
EXPOSE $PORT

# The base image already has the correct startup command