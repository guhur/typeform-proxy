from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typeform import Typeform
from .settings import settings


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

typeform = Typeform(settings.api_key)


@app.get("/liveness")
def read_root():
    return "OK"


@app.get("/forms/{form_id}/responses")
def get_responses(form_id: str, included_response_ids: str | None = None):
    return typeform.responses.list(form_id, includedResponseIds=included_response_ids)  # type: ignore
