# temporary stage
FROM python:3.13-slim as builder

COPY --from=ghcr.io/astral-sh/uv:0.5.2 /uv /bin/uv
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/venv \
    PATH="/venv/bin:$PATH"

COPY uv.lock pyproject.toml  ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev


FROM python:3.13-slim


WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"


COPY . .