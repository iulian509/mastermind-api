from flask import Blueprint, Response


status_bp = Blueprint("status", __name__)


@status_bp.route("/status")
def status():
    return Response(status=200)
