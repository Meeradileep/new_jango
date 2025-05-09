pip install dj-database-url
import dj-database-url
import os
DATABASES = {
 "default": dj_database_url.parse(os.environ.get("postgresql://test_db_864t_user:VcgNwoa8ZhPVv6P8PjnYwukHcsBLx1fs@dpg-d0epfd6mcj7s7382mqjg-a.oregon-postgres.render.com/test_db_864t"))
}
