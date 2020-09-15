[Referance Article](https://dev.to/aymanemx/building-a-full-text-search-app-using-django-docker-and-elasticsearch-3bai)

### Run Commands within Docker

    docker-compose run web python /code/manage.py makemigrations

    docker-compose run web python /code/manage.py migrate

    docker-compose run web python /code/manage.py load_posts 20

    docker-compose run web python /code/manage.py createsuperuser

#### Quick elastic queries

search = PostDocument.search()

# Filter by single field equal to a value

search = search.query('match', draft=False)

# Filter by single field containing a value

search = search.filter('match_phrase', title="value")

# Add the query to the Search object

from elasticsearch_dsl import Q

q = Q("multi_match", query='python django', fields=['title', 'content'])
search = search.query(q)

# Query combination

or_q = Q("match", title='python') | Q("match", title='django')
and_q = Q("match", title='python') & Q("match", title='django')

# Exclude items from your query

search = search.exclude('match', draft=True)

# Filter documents that contain terms within a provided range.

# eg: the posts created for the past day

search = search.filter('range', created_at={"gte": "now-1d"})

# Ordering

# prefixed by the - sign to specify a descending order.

search = search.sort('-likes', 'created_at')
