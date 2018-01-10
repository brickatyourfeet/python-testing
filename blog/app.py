from blog import Blog

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blog, "r" to read, "p" post, "q" quit.'
#three quotes allows for multi line string
POST_TEMPLATE = '''
=-=- {} -=-=   

{}

'''

blogs = dict()  #blog_name: blogObject



def menu():
    #show the user the available blogs
    #let user make choice, do something, exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection =='l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    #print available blogs
    for key, blog in blogs.items():  # [(blog_name, Blog), (blog_name, Blog)] key and value
        print('-{}'.format(blog))

def ask_create_blog():
    title = input('Enter blog title: ')
    author = input('Enter your name: ')

    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input('Enter title of blog you want to read: ')

    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    blog_name = input('Enter your blog to write in: ')
    title = input('Enter post title: ')
    content = input('Enter your post content: ')

    blogs[blog_name].create_post(title,content)


