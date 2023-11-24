<style>
    .custom-title {
        font-family: "Arial", sans-serif;
        font-size: 2.5em;
        text-align: center;
        padding: 10px 0;
        color: #EFEFEF;
        border-bottom: 3px solid #FF6347;
        margin-bottom: 20px;
    }
</style>

<div class="custom-title">Project Manage</div>

# STEP 1: Prepare for the project
- **Git**:version control system that allows multiple people to work on a project at the same time without interfering with each other’s work. 
- **GitHub**：web-based platform that uses Git for version control
- **VSCode**：source-code editor.It supports various programming languages and features.
- **Nodejs**:JavaScript engine.
- **Fontend Language**:MarkDown, HTML, CSS, and JavaScript

# STEP 2: Create a repository
- **Create a new repository** in the GitHub.
![Alt text](../_media/pro01_manage/create_repo.png)
![Alt text](../_media/pro01_manage/create_repo2.png)

# STEP 3: Clone the repository to the local computer

- **Clone the repository** to your local computer.And use GitHub Desktop to manage the repository.
![Alt text](../_media/pro01_manage/clone_repo1.png)
![Alt text](../_media/pro01_manage/copy_url.png)

# STEP 4: Depoly the repository
- **Ensure Source and Branch have been setting**
![Alt text](../_media/pro01_manage/github_branchAndsource.png)
- After setting the source and branch, you can see the website link in the setting page. 
![Alt text](../_media/pro01_manage/website.png)

# STEP 5: Initial the repository
- **Clone the repository** to your local computer.And use GitHub Desktop to manage the repository.
- open the file folder of the repository in the terminal.  
  ![Alt text](../_media/pro01_manage/desktop_finder.png)
- open the terminal in the file folder.
  ![Alt text](../_media/pro01_manage/terminal_file_folder.png)
  - use command to initial the repository.
  ```bash
    npm i docsify-cli -g
    docsify init ./docs
    ```
# STEP 6: Edit code of the website
- You can use VSCode to edit the code.
- ![Alt text](../_media/pro01_manage/vscode.png)
- You can also **preview** the markdown file in VSCode.
![Alt text](../_media/pro01_manage/vscode_editor.png)

# STEP 7: Synchronizing code to GitHub
- After editing the code in VSCode, you can check the changes in the GitHub Desktop.And then you can **commit** the changes. *In Git, the commit process records changes to the repository by capturing a snapshot of the current state of the working directory.*
![Alt text](../_media/pro01_manage/commit_pages.png)

- Before pushing the code to the GitHub, you need to **fetch** and **pull** the code from the GitHub. It is aim to ensure that the code in the local computer is the latest version.
![Alt text](../_media/pro01_manage/fetch_code.png)
![Alt text](../_media/pro01_manage/pull_code.png)
- Last, **push** the code to the GitHub.
![Alt text](../_media/pro01_manage/push_img.png)

Every time after push the code, the website will be **updated automatically**. And you can check the status of the action in the action tap.If the action is failed, you can check the error message in the log.
![Alt text](../_media/pro01_manage/action_status.png)


# Dtails of the code
## Modify index.html to enable some functions
- **Enable the search function**
  ```html
  <script>
    window.$docsify = {
      search: 'auto',
      placeholder: 'Search',
      noData: 'No Results!',
      depth: 3,
    }
  </script>
  ```
- **Enable Navigational Bar and Sidebar**
  ```html
  <script>
    window.$docsify = {
      loadSidebar: true,
      loadNavbar: true,
      subMaxLevel: 3, // 生成目录的最大层级
    }
  </script>
  ```
- **Enable the cover page**
  ```html
  <script>
    window.$docsify = {
      coverpage: true,
    }
  ```
## File Relationship In Fold
To manage the content of the sidebar, you need to edit the _sidebar.md file. And you can set the navigation bar in the _navbar.md file. The content of the cover page is in the _coverpage.md file. They are all in the root folder of the repository. And the files in the _media folder are the images and videos used in the website.
![Alt text](../_media/pro01_manage/file_folder.png)

## Set the sidebar and navigation bar
The `_sidebar.md` file defines the structure and links of the documentation's sidebar navigation, enabling organized access to different sections or pages. Links are structured hierarchically with main topics and sub-topics. You can set the sidebar in the _sidebar.md file.
  ```markdown
  * [About us](md/about_us.md)
    * [Qingling Li](md/lql.md)
    * [Shitong Weng](md/wst.md)
    * [Run Ye](md/yr.md)
    * [Chunxu Zhang](md/zcx.md)
    * [Cuina Zhao](md/zcn.md)
  ```
Similarity , the `_navbar.md` file defines the structure and links of the documentation's navigation bar. You can set the navigation bar in the _navbar.md file.
  ```markdown
  * Links
    * [Reference](https://blog.csdn.net/Mark_md/article/details/121457115)
    * [Polytechnic Institute, ZJU](https://pi.zju.edu.cn/_s991/main.psp)
  ```
Sidebar and navigation bar will be displayed in the website as follows.
![Alt text](../_media/pro01_manage/side_nav_bar_effect.png)
## Set the cover page
Cover page is the first page of the website. You can set the cover page in the _coverpage.md file.

add coverpage: true in the index.html file.
  ```html
  <script>
    window.$docsify = {
      coverpage: true,
    }
  </script>
  ```
 edit the cover page in the[ _coverpage.md](https://github.com/NexMaker-Fab/2023zjudemini-hi1/blob/main/_coverpage.md) file.

   ```markdown
<!-- _coverpage.md -->

![logo](/_media/logo-removebg-preview.png)

# 基因重组 

> Group Portfolio

- Inovativation
- Knowledge
- User-Centric

[GitHub](https://github.com/NexMaker-Fab/2023zjudemini-hi1)
[Get Started](https://nexmaker-fab.github.io/2023zjudemini-hi1/#/md/about_us)
  ```
Cover page will be displayed in the website as follows.
![Alt text](../_media/pro01_manage/coverage.png)
## Personal Introduction page template
```html
<p align="center">
  <img width="150" src="path" alt="name" style="border-radius:50%;">
</p>

<h1 align="center">name</h1>

<p align="center">
self introduction
</p>
## Field

## Skills

## Education

### School Name (Year Started - Year Ended)

## Experiences
### Company Name / Position (Year Started - Year Ended)
- **Role**: 
- **Achievements**: 
```
# How to write our firsr document (Coding method)
```html
<!-- Header -->
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
<!-- Emphasis -->
*italic* or _italic_
**bold** or __bold__
***bold and italic*** or ___bold and italic___
<!-- Lists -->
    <!-- Ordered Lists -->
    1. First item
    2. Second item
    3. Third item
    <!-- Unordered Lists -->
    - Item 1
    - Item 2
        - Subitem 2.1
        - Subitem 2.2
<!-- Links -->
[OpenAI's website](https://www.openai.com/)
<!-- Images -->
![Alt text for the image](URL_to_image.jpg)
<!-- Code -->
`code`
<!-- Add Video -->
<iframe src=[url] width="640" height="480" frameborder="0" scrolling="no"></iframe>

...
```
# How to collaborator team
When add a team to a repository, can assign different roles
- **Read**: Team members can clone the repository and pull, but not push changes.
- **Triage**: Team members can manage issues and pull requests without access to sensitive or destructive actions.
- **Write**: Team members can clone, pull, and push to the repository and manage issues and pull requests.
- **Maintain**: Team members can manage the repository without access to sensitive or destructive actions.
- **Admin**: Team members can fully manage the repository and its settings, including adding or removing collaborators and other administrative actions.

In our case , we set the team as follows.
![Alt text](../_media/pro01_manage/collaborator.jpg)
- **Leadership and Responsibility**: The team leader likely needs administrative privileges to manage the settings of the repository, control access permissions for the team, and handle the most critical operational tasks.
- **Contributor Permissions**: Team contributors are often given "Maintain" roles, which allow them to manage the repository in terms of its content (like handling issues, pull requests, and the project's wiki), without allowing them to change sensitive settings that could affect the repository's visibility or existence.
# How we develop this website
- we create a new [repository](https://github.com/wengstA/fab_hw) in the GitHub.
- And we try to inital the docsify in the local computer. Then push the code to the GitHub. And see the website in the GitHub page.
- As Everything runs well, we copied the code to the repository of the team.**(Keep the same file structure)** Also, there is another way, that is to [fork the repository](https://docs.github.com/articles/fork-a-repo) to the team repository.
# PROBLEMS & SOLUTIONS
## Problem 1: Image cannot be displayed

- **Problem Description**: The image cannot be displayed in the website.
  
- **Solution**: 
  1.   Check the path of Image, and ensure the image is in the _media folder.U can use the relative path to set the image, which can be copied from the VSCode.
  ![Alt text](../_media/pro01_manage/copy_path_vscode.png)
  2.  Copy the image url in the GitHub and paste it in the markdown file.
    ![Alt text](../_media/pro01_manage/copy_img_url.png)
  
  ## Problem 2: The website cannot be updated automatically
  - **Problem Description**: The website cannot be updated automatically after pushing the code to the GitHub. In the action tap, the status of the action is failed.
  - **Solution**:
  Click Build error to see the error message in the log. And then you can find the reason of the error. In this case, the reason is that the theme of the website is wrongly set.  
- ![Alt text](image-2.png)
![Alt text](../_media/pro01_manage/error_showing.png)
![Alt text](../_media/pro01_manage/node_error.png)
Check offical document to see how a theme should be set [Github pages theme setting](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll). And then change the theme in the _config.yml file<br>

    ```
    theme: minima
    ```

# Full Code of index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Fivevolution</title>
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <meta name="description" content="Description">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify-themeable@0/dist/css/theme-simple-dark.css">

</head>
<body>
  <div id="app"></div>
  <script>
    window.$docsify = {
      name: 'Our Space',
      repo: '',
      loadSidebar: true,  //prepare for sidebar
      loadNavbar: true,   //prepare for navbar
      coverpage: true,
      subMaxLevel: 3, // 生成目录的最大层级
      search: 'auto',
      placeholder: 'Search',
      noData: 'No Results!',
      depth: 3,
    }
  </script>
  <!-- Docsify v4 -->
  <script src="//cdn.jsdelivr.net/npm/docsify@4"></script>
</body>
</html>
```