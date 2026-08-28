# Agent Instructions

## Project shape

- This is a Django portal built on `django-globus-portal-framework`.
- Run Django commands through `manage.py`; it defaults to `itmdatacommons.settings.local`.
- Search routes are defined in [itmdatacommons/urls.py](itmdatacommons/urls.py), and the configured `itmdc` Globus Search index lives in [itmdatacommons/settings/base.py](itmdatacommons/settings/base.py).
- The root route renders the `itmdc` search-about page; `<index>/data` handles search requests, while framework and social-auth routes are included beneath the same URL configuration.
- Search result field transforms and Globus links belong in [itmdatacommons/fields.py](itmdatacommons/fields.py).
- Field helpers expect the Globus result shape used by the configured index: a record list whose first record contains keys such as `Name`, `Description`, `DataCategory`, and `Weblink`.
- Framework template overrides are under [itmdatacommons/templates/globus-portal-framework/v2](itmdatacommons/templates/globus-portal-framework/v2); project CSS is under [itmdatacommons/static/custom](itmdatacommons/static/custom).

## Development

- Use Python 3.13 or newer, and keep dependencies synchronized with `pyproject.toml` and `uv.lock`.
- The setup process, including Globus OAuth configuration and local database initialization, is documented in [README.md](README.md).
- Local settings files are intentionally ignored by Git. Never commit Globus secrets, Django secret keys, or other credentials; use a local settings file or environment-based configuration.
- `itmdatacommons` is the active Django package: `ROOT_URLCONF`, WSGI/ASGI, settings, and field imports point there. Verify all import paths before changing package names.

## Validation

- Run `uv run python manage.py check` after Django or settings changes.
- Run focused tests when present; no test suite is currently defined in the repository metadata.
- Keep changes scoped to the owning Django settings, view/URL, template, static asset, or field-transform module. Avoid editing generated/vendor assets unless required.
