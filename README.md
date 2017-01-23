# django-rest-demo
Rest application demonstration
## Models
### Author
* first_name
* last_name
* email

### Book
* title
* page_size
* author (foreign key)

## Usage  
``` bash
git clone git@github.com:She110ck/django-rest-demo.git
# do magick with virtualenv
pip install -r requirements.txt
# do magick with migrations and run

```
Works after authentication (of course you can comment `REST_FRAMEWORK` variable in `settings.py` and work without log in).

|URL                                    | request type | operation            | 
| ------------------------------------  |:------------:| --------------------:|
|`http://localhost:8000/api/authors/`   | GET          | list of authors      |
|`http://localhost:8000/api/books/`     | GET          | list of books        |
|`http://localhost:8000/api/books-adv/` | GET          | advanced list        |
|`http://localhost:8000/api/authors/`   | POST         | add new author       |
|`http://localhost:8000/api/books/`     | POST         | add new book         |
|`http://localhost:8000/api/authors/1/` | PUT          | edit current author  |
|`http://localhost:8000/api/book/1/`    | PUT          | edit current book    |
|`http://localhost:8000/api/author/1/`  | DELETE       | delete current author|
|`http://localhost:8000/api/book/1/`    | DELETE       | delete currentbook   |

## Serialization
`serialize.py` contains serializers.

## Branches
### master branch

master branch uses viewsets. In `viewset.py` defined viewsets and router.

### origin branch
origin branch uses class-based views inherited APIView.  
File `views.py` contains custom class-based views.  
File `generic_views.py` contains generic class-based views. Generic views uses `/api-gen/` url prefix.  
Example: `http://localhost:8000/api-gen/books/`

You can switch branches with: `git checkout <branch_name>`

### Good Luck!
