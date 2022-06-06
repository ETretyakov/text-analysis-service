from dotenv import load_dotenv

from app.core.config import Settings

load_dotenv()

settings = Settings()

from app.documents.models import Document  # noqa
from app.ontologies.models import Metric  # noqa
