from flask import Blueprint, render_template, redirect

from project.models import URI_Table

route_bp = Blueprint('route_bp', __name__)


@route_bp.route('/', defaults={'path': ''}, methods=['GET'])
@route_bp.route('/<path:path>', methods=['GET'])
def redirect_to_original(path):

    # ID not specified.
    if path == '':
        return render_template('error.html')
    try:
        # Get original uri by ID.
        uri = URI_Table.query.filter_by(short_url=path).first()
        # Redirect to original page.
        return redirect(uri.original_url)

    except:
        return render_template('error.html')
