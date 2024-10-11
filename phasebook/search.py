from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    user_query = []

    id_filter = request.args.get("id")
    name_filter = request.args.get("name")
    age_filter = request.args.get("age")
    occupation_filter = request.args.get("occupation")
    

    if id_filter:
        user_query = [user for user in USERS if user['id'] == id_filter]

    if name_filter:
        user_query = user_query + [user for user in USERS if name_filter.lower() in user['name'].lower() and user not in user_query]
        
    if age_filter:
        age_input = int(args['age'])
        user_query = user_query + [user for user in USERS if age_input -1 <= user['age'] <= age_input +1 and user not in user_query]

    if occupation_filter:
        user_query = user_query + [user for user in USERS if occupation_filter.lower() in user['occupation'].lower() and user not in user_query]

    if not id_filter and not name_filter and not age_filter and not occupation_filter:
        user_query= USERS

    return user_query
