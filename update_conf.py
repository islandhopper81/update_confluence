import os
from atlassian import Confluence

my_url = os.environ.get("URL")
my_name = os.environ.get("NAME")
my_secret = os.environ.get("SECRET")
my_space_key = os.environ.get("SPACE_KEY")
my_page_title = os.environ.get("PAGE_TITLE")

confluence = Confluence(
  ulr=my_url,
  username=my_name,
  password=my_secret
)

page_id = confluence.page_id(my_space_key, my_page_title)

page = confluence.get_page_by_id(page_id, expand='body.storage')

# update the content on the page
page['body']['storage']['value'] = "New Content"
page['body']['storage']['representation'] = "storage"

# save the changes
confluence.update_page(page, validate_version=True)
