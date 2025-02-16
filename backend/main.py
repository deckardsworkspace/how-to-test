import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.views.text.router import router as TextRouter

# Create FastAPI app
app = FastAPI(title='backend')
app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['Authorization', 'Content-Type'],
)

# Add routes
app.include_router(TextRouter, prefix='/text')


if __name__ == '__main__':
  uvicorn.run(
    app='backend.main:app',
    host='0.0.0.0',
    port=12345,
    reload=True,
  )
