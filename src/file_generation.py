import os, shutil
from textnode import TextNode
from block_util import markdown_to_html_node

def static_to_public(src, dst):
    #should first delete all contents of the destination directory
    print(src, dst)
    if os.path.exists(dst):
        shutil.rmtree(dst)
    
    recursive_call(src, dst)

def recursive_call(src, dst):
    print(os.listdir(src))
    if not os.path.isfile(src):
        #if its a directory
        os.mkdir(dst)
    for item in os.listdir(src):
        new_source = os.path.join(src, item)
        new_dst = os.path.join(dst, item)
        if not os.path.isfile(new_source):
            recursive_call(new_source, new_dst)
        else:
            shutil.copy(new_source, new_dst)
        
def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        stripped_line = line.strip()
        if stripped_line[:2] == '# ':
            return stripped_line[2:]

def generate_page(from_path, template_path, dest_path):
    print(f'generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path, 'r') as markdown_file:
        markdown_file_contents = markdown_file.read()
    # print(markdown_file_contents, 'THIS IS MARKDOWN CONTENTS')
    with open(template_path, 'r') as template_file:
        template_file_contents = template_file.read()

    markdown_to_html_node_now = markdown_to_html_node(markdown_file_contents)
    html_string = markdown_to_html_node_now.to_html()
    title = extract_title(markdown_file_contents)

    content_added = template_file_contents.replace("{{ Content }}", html_string)
    title_added = content_added.replace("{{ Title }}", title)

    directory_for_dest = os.path.dirname(dest_path)
    os.makedirs(directory_for_dest, exist_ok=True)
    
    with open(dest_path, 'w') as file:
        file.write(title_added)