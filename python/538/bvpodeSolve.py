<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta charset="utf-8">
  <title>
  mmorse1217 / Mth437 
  / source  / mth438 / classCode / bvpodeSolve.py
 &mdash; Bitbucket
</title>
  <link rel="icon" type="image/png" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/ea3b2d752f06/img/favicon.png">
  <meta id="bb-canon-url" name="bb-canon-url" content="https://bitbucket.org">
  
  
    
<link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/ea3b2d752f06/compressed/css/a96bf0033881.css" type="text/css" />
<link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/ea3b2d752f06/compressed/css/3a60558b3613.css" type="text/css" />

  
  <!--[if lt IE 9]><link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/ea3b2d752f06//lib/aui/css/aui-ie.css" media="all"><![endif]-->
  <!--[if IE 9]><link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/ea3b2d752f06//lib/aui/css/aui-ie9.css" media="all"><![endif]-->
  <!--[if IE]><link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/ea3b2d752f06/css/aui-overrides-ie.css" media="all"><![endif]-->
  <meta name="description" content=""/>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="Bitbucket" />
  
  
    <link href="/mmorse1217/mth437/rss" rel="alternate nofollow" type="application/rss+xml" title="RSS feed for Mth437" />
  

<script type="text/javascript">var NREUMQ=NREUMQ||[];NREUMQ.push(["mark","firstbyte",new Date().getTime()]);</script></head>
<body class="production "
      data-base-url="https://bitbucket.org"
      data-no-avatar-image="https://d3oaxc4q5k2d6q.cloudfront.net/m/ea3b2d752f06/img/default_avatar/16/user_blue.png"
      data-current-user="{&quot;isKbdShortcutsEnabled&quot;: true, &quot;isSshEnabled&quot;: false, &quot;isAuthenticated&quot;: false}"
      
      
       data-current-repo="{&quot;scm&quot;: &quot;git&quot;, &quot;readOnly&quot;: false, &quot;mainbranch&quot;: {&quot;name&quot;: &quot;master&quot;}, &quot;language&quot;: &quot;python&quot;, &quot;creator&quot;: {&quot;username&quot;: &quot;mmorse1217&quot;}, &quot;owner&quot;: {&quot;username&quot;: &quot;mmorse1217&quot;, &quot;isTeam&quot;: false}, &quot;fullslug&quot;: &quot;mmorse1217/mth437&quot;, &quot;slug&quot;: &quot;mth437&quot;, &quot;id&quot;: 1307929, &quot;pygmentsLanguage&quot;: &quot;python&quot;}"
       data-current-cset="e6d99754ba43b2d85d8aa950bad3436b8483920c"
      
      
      
      >
<script type="text/javascript" src="https://d3oaxc4q5k2d6q.cloudfront.net/m/ea3b2d752f06/compressed/js/7a107bcc2ab3.js"></script>

<div id="page">
  <div id="wrapper">
    
  


    <header id="header" role="banner">
      
  
    
  

      <nav class="aui-header aui-dropdown2-trigger-group" role="navigation">
        <div class="aui-header-inner">
          <div class="aui-header-primary">
            
  

            
              <h1 class="aui-header-logo aui-header-logo-bitbucket logged-out">
                <a href="/" class="aui-nav-imagelink" id="logo">
                  <span class="aui-header-logo-device">Bitbucket</span>
                </a>
              </h1>
            
            
  <script id="repo-dropdown-template" type="text/html">
  

[[#hasViewed]]
  <div class="aui-dropdown2-section">
    <strong class="viewed">Recently viewed</strong>
    <ul class="aui-list-truncate">
      [[#viewed]]
        <li class="[[#is_private]]private[[/is_private]][[^is_private]]public[[/is_private]] repository">
          <a href="[[url]]" title="[[owner]]/[[name]]" class=" aui-icon-container">
            <img class="repo-avatar size16" src="[[{avatar}]]" alt="[[owner]]/[[name]] avatar"/>
            [[owner]] / [[name]]
          </a>
        </li>
      [[/viewed]]
    </ul>
  </div>
[[/hasViewed]]
[[#hasUpdated]]
<div class="aui-dropdown2-section">
  <strong class="updated">Recently updated</strong>
  <ul class="aui-list-truncate">
    [[#updated]]
    <li class="[[#is_private]]private[[/is_private]][[^is_private]]public[[/is_private]] repository">
      <a href="[[url]]" title="[[owner]]/[[name]]" class=" aui-icon-container">
        <img class="repo-avatar size16" src="[[{avatar}]]" alt="[[owner]]/[[name]] avatar"/>
        [[owner]] / [[name]]
      </a>
    </li>
    [[/updated]]
  </ul>
</div>
[[/hasUpdated]]

</script>
  <ul role="menu" class="aui-nav">
    
      <li>
        <a href="/plans">
            Pricing
        </a>
      </li>
      <li>
        <a href="/whats-new">
          Latest features
        </a>
      </li>
    
  </ul>

          </div>
          <div class="aui-header-secondary">
            
  <ul role="menu" class="aui-nav">
    <li>
      <form action="/repo/all" method="get" class="aui-quicksearch">
        <label for="search-query" class="assistive">owner/repository</label>
        <input id="search-query" class="search" type="text" placeholder="owner/repository" name="name">
      </form>
    </li>
    <li>
      <a class="aui-dropdown2-trigger" aria-controls="header-help-dropdown" aria-owns="header-help-dropdown"
         aria-haspopup="true" data-container="#header .aui-header-inner" href="#header-help-dropdown">
        <span class="aui-icon aui-icon-small aui-iconfont-help">Help</span><span class="aui-icon-dropdown"></span>
      </a>
      <nav id="header-help-dropdown" class="aui-dropdown2 aui-style-default aui-dropdown2-in-header" aria-hidden="true">
        <div class="aui-dropdown2-section">
          <ul>
            <li>
              <a href="/whats-new" id="features-link">
                Latest features
              </a>
            </li>
          </ul>
        </div>
        <div class="aui-dropdown2-section">
          <ul>
            <li>
              <a class="support-ga"
                 data-support-gaq-page="DocumentationHome"
                 href="https://confluence.atlassian.com/x/bgozDQ"
                 target="_blank">
                Documentation
              </a>
            </li>
            <li>
              <a class="support-ga"
                 data-support-gaq-page="Documentation101"
                 href="https://confluence.atlassian.com/x/cgozDQ"
                 target="_blank">
                Bitbucket 101
              </a>
            </li>
            <li>
              <a class="support-ga"
                 data-support-gaq-page="DocumentationKB"
                 href="https://confluence.atlassian.com/x/2w4zDQ"
                 target="_blank">
                Knowledge base
              </a>
            </li>
          </ul>
        </div>
        <div class="aui-dropdown2-section">
          <ul>
            <li>
              <a class="support-ga"
                 data-support-gaq-page="Answers"
                 href="https://answers.atlassian.com/tags/bitbucket/"
                 target="_blank">
                Bitbucket on Atlassian Answers
              </a>
            </li>
            <li>
              <a class="support-ga"
                 data-support-gaq-page="Home"
                 href="/support">
              Support
            </a>
            </li>
          </ul>
        </div>
      </nav>
    </li>
      
        
          <li>
            <a class="aui-dropdown2-trigger" href="#header-language"
              aria-controls="header-language" aria-owns="header-language"
              aria-haspopup="true" data-container="#header .aui-header-inner">
              <span>English</span></a>
            <nav id="header-language" class="aui-dropdown2 aui-style-default aui-dropdown2-radio aui-dropdown2-in-header"
                aria-hidden="true">
              <form method="post" action="/account/language/setlang/">
                <div style='display:none'><input type='hidden' name='csrfmiddlewaretoken' value='dcQfF6PE0PIFgsSCABjz9hlXeT0PHdq7' /></div>
                <input type="hidden" name="language" value="">
                <ul>
                <li><a class="aui-dropdown2-radio interactive checked"
                      data-value="en" href="#en">English</a></li>
                
                <li><a class="aui-dropdown2-radio interactive "
                      data-value="ja" href="#ja">日本語</a></li>
                </ul>
              </form>
            </nav>
          </li>
        
      
    
        <li id="header-signup-button">
          <a id="sign-up-link" class="aui-button aui-button-primary aui-style" href="/account/signup/">
            Sign up
          </a>
        </li>
      <li id="user-options">
        
          
            <a href="/account/signin/?next=/mmorse1217/mth437/src/e6d99754ba43b2d85d8aa950bad3436b8483920c/mth438/classCode/bvpodeSolve.py%3Fat%3Dmaster" class="aui-nav-link login-link">Log in</a>
          
        
      </li>
    
  </ul>

          </div>
        </div>
      </nav>
    </header>

    
  <header id="account-warning" role="banner"
          class="aui-message-banner warning
                ">
    <div class="center-content">
      <span class="aui-icon aui-icon-warning"></span>
      <span class="message">
        
      </span>
    </div>
  </header>

    
    
      <header id="aui-message-bar">
        
      </header>
    


    
  <header id="repo-warning" role="banner" class="aui-message-banner warning">
    <div class="center-content">
      <span class="aui-icon aui-icon-warning"></span>
      <span class="message">
      </span>
    </div>
  </header>
  <script id="repo-warning-template" type="text/html">
  




  This repository's ownership is pending transfer to <a href="/[[username]]">[[username]]</a>.
  Visit the <a href="/mmorse1217/mth437/admin/transfer">transfer repository page</a> to view more details.


</script>
  <header id="repo-header" class="subhead row" data-modules="repo/index">
    <div class="center-content">
      <div class="repo-summary with-repo-watch">
        <a class="repo-avatar-link" href="/mmorse1217/mth437">
           <span class="repo-avatar-container size64" title="mmorse1217/Mth437">
  <img alt="mmorse1217/Mth437" src="https://d3oaxc4q5k2d6q.cloudfront.net/m/ea3b2d752f06/img/language-avatars/python_64.png">
</span>

          
        </a>
        <h1><a class="repo-link" href="/mmorse1217/mth437">Mth437</a></h1>
        <ul class="repo-metadata clearfix">
          <li>
            <a class="user" href="/mmorse1217">
              <span class="aui-icon aui-icon-small aui-iconfont-user">User icon</span>
              <span>mmorse1217</span>
            </a>
          </li>
          
          
          
        </ul>
      </div>
      <div id="repo-toolbar" class="bb-toolbar">
        
          <div class="aui-buttons">
            <a id="repo-clone-button" class="aui-button"
              href="https://bitbucket.org/mmorse1217/mth437.git">
              <span class="aui-icon aui-icon-small aui-iconfont-devtools-clone"></span>
              <span>Clone</span>
              <span class="aui-icon-dropdown"></span>
            </a>
            
              
                <a id="fork-button" class="aui-button"
                   href="/mmorse1217/mth437/fork">
                  <span class="aui-icon aui-icon-small aui-iconfont-devtools-fork"></span>
                  <span>Fork</span>
                </a>
              
              <a id="compare-button" class="aui-button"
                 
                   href="/mmorse1217/mth437/branches/compare">
                 
                <span class="aui-icon aui-icon-small aui-iconfont-devtools-compare"></span>
                <span>Compare</span>
              </a>
            
          </div>
        
        
        

<div id="repo-clone-dialog" class="clone-dialog hidden">
  
<div class="clone-url">
  <div class="aui-buttons">
    <a href="https://bitbucket.org/mmorse1217/mth437.git"
       class="aui-button aui-style aui-dropdown2-trigger" aria-haspopup="true"
       aria-owns="clone-url-dropdown-header">
      <span class="dropdown-text">HTTPS</span>
    </a>
    <div id="clone-url-dropdown-header" class="aui-dropdown2 aui-style-default">
      <ul class="aui-list-truncate">
        <li>
          <a href="https://bitbucket.org/mmorse1217/mth437.git"
            
              data-command="git clone https://bitbucket.org/mmorse1217/mth437.git"
            
            class="item-link https">HTTPS
          </a>
        </li>
        <li>
          <a href="ssh://git@bitbucket.org/mmorse1217/mth437.git"
            
              data-command="git clone git@bitbucket.org:mmorse1217/mth437.git"
            
            class="item-link ssh">SSH
          </a>
        </li>
      </ul>
    </div>
    <input type="text" readonly="readonly" value="git clone https://bitbucket.org/mmorse1217/mth437.git">
  </div>
  
  <p>Need help cloning? Visit
     <a href="https://confluence.atlassian.com/x/cgozDQ" target="_blank">Bitbucket 101</a>.</p>
  
</div>


  
  
  

<div class="sourcetree-callout clone-in-sourcetree"
  data-https-url="https://bitbucket.org/mmorse1217/mth437.git"
  data-ssh-url="ssh://git@bitbucket.org/mmorse1217/mth437.git">

  <div>
    <button class="aui-button aui-style aui-button-primary">
      
        Clone in SourceTree
      
    </button>
  </div>

  <p class="windows-text">
      
        <a href="http://www.sourcetreeapp.com/?utm_source=internal&amp;utm_medium=link&amp;utm_campaign=clone_repo_win" target="_blank">Atlassian SourceTree</a>
        is a free Git and Mercurial client for Windows.
      
  </p>
  <p class="mac-text">
      
        <a href="http://www.sourcetreeapp.com/?utm_source=internal&amp;utm_medium=link&amp;utm_campaign=clone_repo_mac" target="_blank">Atlassian SourceTree</a>
        is a free Git and Mercurial client for Mac.
      
  </p>
</div>

  
</div>

        <div id="repo-more-dropdown" class="aui-dropdown2 aui-style-default">
          <ul>
            <li>
              <a id="compare-button"
                 
                   href="/mmorse1217/mth437/branches/compare">
                 
                Compare
              </a>
            </li>
            
              <li>
                <a id="fork-button" href="/mmorse1217/mth437/fork">
                  Fork
                </a>
              </li>
            
          </ul>
        </div>
        
      </div>
    </div>
    <div class="clearfix"></div>
  </header>
  <nav id="repo-tabs" class="aui-navgroup aui-navgroup-horizontal aui-navgroup-horizontal-roomy">
    <div class="aui-navgroup-inner">
      <div class="aui-navgroup-primary">
        <ul class="aui-nav">
          
            <li>
              <a href="/mmorse1217/mth437/overview" id="repo-overview-link">Overview</a>
            </li>
          
          
            <li class="aui-nav-selected">
              <a href="/mmorse1217/mth437/src" id="repo-source-link">Source</a>
            </li>
          
          
            <li>
              <a href="/mmorse1217/mth437/commits" id="repo-commits-link">
                Commits
              </a>
            </li>
          
          
            <li>
              <a href="/mmorse1217/mth437/branches" id="repo-branches-link">
                Branches
              </a>
            </li>
          
          
            <li>
              <a href="/mmorse1217/mth437/pull-requests" id="repo-pullrequests-link">
                Pull requests
                
                  
                
              </a>
            </li>
          
          
            
          
            <li id="issues-tab" class="
              
                hidden
              
            ">
              <a href="/mmorse1217/mth437/issues?status=new&amp;status=open" id="repo-issues-link">
                Issues
                
                  
                
              </a>
            </li>
            <li id="wiki-tab" class="
                
                  hidden
                
              ">
              <a href="/mmorse1217/mth437/wiki" id="repo-wiki-link">Wiki</a>
            </li>
          
            <li>
            <a href="/mmorse1217/mth437/downloads" id="repo-downloads-link">
              Downloads
              
                
              
            </a>
            </li>
          
        </ul>
      </div>
      <div class="aui-navgroup-secondary">
        <ul class="aui-nav">
          
        </ul>
      </div>
    </div>
  </nav>


    <div id="content" role="main">
      
  <div id="repo-content">
    
  <div id="source-container" data-modules="repo/source/index">
    



<header id="source-path">
  
  <div class="labels labels-csv">
    
      <div class="aui-buttons">
        <button data-branches-tags-url="/api/1.0/repositories/mmorse1217/mth437/branches-tags"
                data-modules="components/branch-dialog"
                class="aui-button branch-dialog-trigger" title="master">
          
            
              <span class="aui-icon aui-icon-small aui-iconfont-devtools-branch">Branch</span>
            
            <span class="name">master</span>
          
          <span class="aui-icon-dropdown"></span>
        </button>
        <button class="aui-button" id="checkout-branch-button"
                title="Check out this branch">
          <span class="aui-icon aui-icon-small aui-iconfont-devtools-clone">Check out branch</span>
          <span class="aui-icon-dropdown"></span>
        </button>
      </div>
      <script id="branch-checkout-template" type="text/html">
  

<div id="checkout-branch-contents">
  <div class="command-line">
    <p>
      Check out this branch on your local machine to begin working on it.
    </p>
    <input type="text" class="checkout-command" readonly="readonly"
        
           value="git fetch && git checkout [[branchName]]"
        
        >
  </div>
  
    

<div class="sourcetree-callout clone-in-sourcetree"
  data-https-url="https://bitbucket.org/mmorse1217/mth437.git"
  data-ssh-url="ssh://git@bitbucket.org/mmorse1217/mth437.git">

  <div>
    <button class="aui-button aui-style aui-button-primary">
      
        Check out in SourceTree
      
    </button>
  </div>

  <p class="windows-text">
      
        <a href="http://www.sourcetreeapp.com/?utm_source=internal&amp;utm_medium=link&amp;utm_campaign=clone_repo_win" target="_blank">Atlassian SourceTree</a>
        is a free Git and Mercurial client for Windows.
      
  </p>
  <p class="mac-text">
      
        <a href="http://www.sourcetreeapp.com/?utm_source=internal&amp;utm_medium=link&amp;utm_campaign=clone_repo_mac" target="_blank">Atlassian SourceTree</a>
        is a free Git and Mercurial client for Mac.
      
  </p>
</div>

  
</div>
</script>
    
  </div>
  
  
    <div class="view-switcher">
      <div class="aui-buttons">
        
          <a href="/mmorse1217/mth437/src/e6d99754ba43/mth438/classCode/bvpodeSolve.py?at=master"
             class="aui-button aui-style pjax-trigger" aria-pressed="true">
            Source
          </a>
          <a href="/mmorse1217/mth437/diff/mth438/classCode/bvpodeSolve.py?diff2=e6d99754ba43&at=master"
             class="aui-button aui-style pjax-trigger"
             title="Diff to previous change">
            Diff
          </a>
          <a href="/mmorse1217/mth437/history-node/e6d99754ba43/mth438/classCode/bvpodeSolve.py?at=master"
             class="aui-button aui-style pjax-trigger">
            History
          </a>
        
      </div>
    </div>
  
  <h1>
    <a href="/mmorse1217/mth437/src/e6d99754ba43?at=master"
       class="pjax-trigger" title="mmorse1217/mth437 at e6d99754ba43">Mth437</a> /
    
      
        
          
            <a href="/mmorse1217/mth437/src/e6d99754ba43/mth438/?at=master"
               class="pjax-trigger">mth438</a> /
          
        
      
    
      
        
          
            <a href="/mmorse1217/mth437/src/e6d99754ba43/mth438/classCode/?at=master"
               class="pjax-trigger">classCode</a> /
          
        
      
    
      
        
          <span>bvpodeSolve.py</span>
        
      
    
  </h1>
  
    
    
  
  <div class="clearfix"></div>
</header>


    <div id="editor-container" class="maskable"
         data-owner="mmorse1217"
         data-slug="mth437"
         data-is-writer="false"
         data-has-push-access="true"
         data-hash="e6d99754ba43b2d85d8aa950bad3436b8483920c"
         data-branch="master"
         data-path="mth438/classCode/bvpodeSolve.py"
         data-source-url="/api/1.0/repositories/mmorse1217/mth437/src/e6d99754ba43b2d85d8aa950bad3436b8483920c/mth438/classCode/bvpodeSolve.py">
      <div id="source-view" data-modules="repo/source/view-file">
        <div class="toolbar">
          <div class="primary">
            <div class="aui-buttons">
              
                <button id="file-history-trigger" class="aui-button aui-style changeset-info"
                        data-changeset="e6d99754ba43b2d85d8aa950bad3436b8483920c"
                        data-path="mth438/classCode/bvpodeSolve.py"
                        data-current="e6d99754ba43b2d85d8aa950bad3436b8483920c">
                  
                     

<img class="avatar avatar16" src="https://d3oaxc4q5k2d6q.cloudfront.net/m/ea3b2d752f06/img/default_avatar/16/user_blue.png" alt="Anonymous avatar" />
<span class="changeset-hash">e6d9975</span>
<time datetime="2013-04-22T01:29:57+00:00" class="timestamp"></time>
<span class="aui-icon-dropdown"></span>

                  
                </button>
              
            </div>
          <a href="/mmorse1217/mth437/full-commit/e6d99754ba43/mth438/classCode/bvpodeSolve.py" id="full-commit-link"
              title="View full commit e6d9975">Full commit</a>
          </div>
            <div class="secondary">
              <div class="aui-buttons">
                
                  <a href="/mmorse1217/mth437/annotate/e6d99754ba43b2d85d8aa950bad3436b8483920c/mth438/classCode/bvpodeSolve.py?at=master"
                  class="aui-button aui-style pjax-trigger">Blame</a>
                
                
                  
                  <a id="embed-link" href="https://bitbucket.org/mmorse1217/mth437/src/e6d99754ba43b2d85d8aa950bad3436b8483920c/mth438/classCode/bvpodeSolve.py?embed=t"
                    class="aui-button aui-style">Embed</a>
                
                <a href="/mmorse1217/mth437/raw/e6d99754ba43b2d85d8aa950bad3436b8483920c/mth438/classCode/bvpodeSolve.py"
                  class="aui-button aui-style">Raw</a>
              </div>
              
            </div>
          <div class="clearfix"></div>
        </div>

        
          
            
              
                <div class="file-source">
                  <table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><a href="#cl-1"> 1</a>
<a href="#cl-2"> 2</a>
<a href="#cl-3"> 3</a>
<a href="#cl-4"> 4</a>
<a href="#cl-5"> 5</a>
<a href="#cl-6"> 6</a>
<a href="#cl-7"> 7</a>
<a href="#cl-8"> 8</a>
<a href="#cl-9"> 9</a>
<a href="#cl-10">10</a>
<a href="#cl-11">11</a>
<a href="#cl-12">12</a>
<a href="#cl-13">13</a>
<a href="#cl-14">14</a>
<a href="#cl-15">15</a>
<a href="#cl-16">16</a>
<a href="#cl-17">17</a>
<a href="#cl-18">18</a>
<a href="#cl-19">19</a>
<a href="#cl-20">20</a>
<a href="#cl-21">21</a>
<a href="#cl-22">22</a>
<a href="#cl-23">23</a>
<a href="#cl-24">24</a>
<a href="#cl-25">25</a>
<a href="#cl-26">26</a>
<a href="#cl-27">27</a>
<a href="#cl-28">28</a>
<a href="#cl-29">29</a>
<a href="#cl-30">30</a>
<a href="#cl-31">31</a>
<a href="#cl-32">32</a>
<a href="#cl-33">33</a>
<a href="#cl-34">34</a></pre></div></td><td class="code"><div class="highlight"><pre><a name="cl-1"></a><span class="kn">from</span> <span class="nn">numpy</span> <span class="kn">import</span> <span class="o">*</span>
<a name="cl-2"></a><span class="kn">from</span> <span class="nn">scipy.optimize</span> <span class="kn">import</span> <span class="n">brentq</span>
<a name="cl-3"></a>
<a name="cl-4"></a>
<a name="cl-5"></a><span class="k">def</span> <span class="nf">euler</span><span class="p">(</span><span class="n">f</span><span class="p">,</span><span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">,</span><span class="n">ya</span><span class="p">,</span><span class="n">n</span><span class="p">):</span>
<a name="cl-6"></a>        <span class="c">#no changes to solve linear system of ODE&#39;s</span>
<a name="cl-7"></a>        <span class="n">h</span> <span class="o">=</span> <span class="p">(</span><span class="n">b</span><span class="o">-</span><span class="n">a</span><span class="p">)</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
<a name="cl-8"></a>        <span class="n">w</span> <span class="o">=</span> <span class="n">array</span><span class="p">(</span><span class="n">ya</span><span class="p">)</span>
<a name="cl-9"></a>        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">n</span><span class="p">):</span>
<a name="cl-10"></a>                <span class="n">t</span> <span class="o">=</span> <span class="n">a</span> <span class="o">+</span> <span class="n">i</span><span class="o">*</span><span class="n">h</span>
<a name="cl-11"></a>                <span class="n">w</span> <span class="o">+=</span> <span class="n">h</span> <span class="o">*</span> <span class="n">f</span><span class="p">(</span><span class="n">t</span><span class="p">,</span><span class="n">w</span><span class="p">)</span>
<a name="cl-12"></a>        <span class="k">return</span> <span class="n">w</span><span class="p">;</span>
<a name="cl-13"></a>
<a name="cl-14"></a><span class="k">def</span> <span class="nf">f</span><span class="p">(</span><span class="n">t</span><span class="p">,</span><span class="n">y</span><span class="p">,</span><span class="n">yprime</span><span class="p">):</span>
<a name="cl-15"></a>	<span class="k">return</span> <span class="o">-</span><span class="mf">9.8</span> <span class="o">-</span> <span class="o">.</span><span class="mi">1</span><span class="o">*</span><span class="n">yprime</span><span class="o">*</span><span class="nb">abs</span><span class="p">(</span><span class="n">yprime</span><span class="p">)</span> <span class="c">#nonlinear damping</span>
<a name="cl-16"></a>
<a name="cl-17"></a><span class="k">def</span> <span class="nf">myF</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">Y</span><span class="p">):</span>
<a name="cl-18"></a>	<span class="k">return</span> <span class="n">array</span><span class="p">([</span><span class="n">Y</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">f</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">Y</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">Y</span><span class="p">[</span><span class="mi">1</span><span class="p">])])</span>
<a name="cl-19"></a>
<a name="cl-20"></a>
<a name="cl-21"></a><span class="k">def</span> <span class="nf">g</span><span class="p">(</span><span class="n">ypa</span><span class="p">):</span>
<a name="cl-22"></a>	<span class="k">global</span> <span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">,</span><span class="n">ya</span><span class="p">,</span><span class="n">yb</span>
<a name="cl-23"></a>	<span class="k">print</span> <span class="n">ypa</span>
<a name="cl-24"></a>	<span class="n">Yatb</span> <span class="o">=</span> <span class="n">euler</span><span class="p">(</span><span class="n">myF</span><span class="p">,</span><span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">,[</span><span class="n">ya</span><span class="p">,</span><span class="n">ypa</span><span class="p">],</span> <span class="mi">1000</span><span class="p">)</span>
<a name="cl-25"></a>	<span class="k">return</span> <span class="n">Yatb</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">-</span> <span class="n">yb</span>
<a name="cl-26"></a>
<a name="cl-27"></a><span class="n">a</span><span class="o">=</span><span class="mi">0</span>
<a name="cl-28"></a><span class="n">b</span><span class="o">=.</span><span class="mi">5</span>
<a name="cl-29"></a><span class="n">ya</span> <span class="o">=</span> <span class="mf">0.1</span>
<a name="cl-30"></a><span class="n">yb</span> <span class="o">=</span> <span class="mf">1.</span>
<a name="cl-31"></a><span class="n">ypa1</span> <span class="o">=</span> <span class="mf">0.</span>
<a name="cl-32"></a><span class="n">ypa2</span> <span class="o">=</span> <span class="mf">10.</span>
<a name="cl-33"></a>
<a name="cl-34"></a><span class="k">print</span> <span class="n">brentq</span><span class="p">(</span><span class="n">g</span><span class="p">,</span><span class="n">ypa1</span><span class="p">,</span><span class="n">ypa2</span><span class="p">)</span>
</pre></div>
</td></tr></table>
                </div>
              
            
          
        
      </div>
    </div>



<div class="mask"></div>



  <script id="branch-dialog-template" type="text/html">
  

<div class="tabbed-filter-widget branch-dialog">
  <div class="tabbed-filter">
    <input placeholder="Filter branches" class="filter-box" autosave="branch-dropdown-1307929" type="text">
    [[^ignoreTags]]
      <div class="aui-tabs horizontal-tabs aui-tabs-disabled filter-tabs">
        <ul class="tabs-menu">
          <li class="menu-item active-tab"><a href="#branches">Branches</a></li>
          <li class="menu-item"><a href="#tags">Tags</a></li>
        </ul>
      </div>
    [[/ignoreTags]]
  </div>
  
    <div class="tab-pane active-pane" id="branches" data-filter-placeholder="Filter branches">
      <ol class="filter-list">
        <li class="empty-msg">No matching branches</li>
        [[#branches]]
          
            [[#hasMultipleHeads]]
              [[#heads]]
                <li class="comprev filter-item">
                  <a class="pjax-trigger" href="/mmorse1217/mth437/src/[[changeset]]/mth438/classCode/bvpodeSolve.py?at=[[safeName]]"
                     title="[[name]]">
                    [[name]] ([[shortChangeset]])
                  </a>
                </li>
              [[/heads]]
            [[/hasMultipleHeads]]
            [[^hasMultipleHeads]]
              <li class="comprev filter-item">
                <a class="pjax-trigger" href="/mmorse1217/mth437/src/[[changeset]]/mth438/classCode/bvpodeSolve.py?at=[[safeName]]" title="[[name]]">
                  [[name]]
                </a>
              </li>
            [[/hasMultipleHeads]]
          
        [[/branches]]
      </ol>
    </div>
    <div class="tab-pane" id="tags" data-filter-placeholder="Filter tags">
      <ol class="filter-list">
        <li class="empty-msg">No matching tags</li>
        [[#tags]]
          <li class="comprev filter-item">
            <a class="pjax-trigger" href="/mmorse1217/mth437/src/[[changeset]]/mth438/classCode/bvpodeSolve.py?at=[[safeName]]" title="[[name]]">
              [[name]]
            </a>
          </li>
        [[/tags]]
      </ol>
    </div>
  
</div>

</script>



  </div>

  </div>
  

<form id="file-search-form" action="#"
  
  data-revision="e6d99754ba43b2d85d8aa950bad3436b8483920c"
  data-branch="master">
  <input type="text" id="file-search-query" class="loading">
  <div id="filtered-files"></div>
  <div class="tip"><em>Tip:</em> Filter by directory path e.g. <strong>/media app.js</strong> to search for public<strong>/media/app.js</strong>.</div>
  <div class="tip"><em>Tip:</em> Use camelCasing e.g. <strong>ProjME</strong> to search for <strong>ProjectModifiedE</strong>vent.java.</div>
  <div class="tip"><em>Tip:</em> Filter by extension type e.g. <strong>/repo .js</strong> to search for all <strong>.js</strong> files in the <strong>/repo</strong> directory.</div>
  <div class="tip"><em>Tip:</em> Separate your search with spaces e.g. <strong>/ssh pom.xml</strong> to search for src<strong>/ssh/pom.xml</strong>.</div>
  <div class="tip"><em>Tip:</em> Use ↑ and ↓ arrow keys to navigate and <strong>return</strong> to view the file.</div>
  <div class="tip mod-osx"><em>Tip:</em> You can also navigate files with <strong>Ctrl+j</strong> <em>(next)</em> and <strong>Ctrl+k</strong> <em>(previous)</em> and view the file with <strong>Ctrl+o</strong>.</div>
  <div class="tip mod-win"><em>Tip:</em> You can also navigate files with <strong>Alt+j</strong> <em>(next)</em> and <strong>Alt+k</strong> <em>(previous)</em> and view the file with <strong>Alt+o</strong>.</div>
  <script id="filtered-files-template" type="text/html">
  

<table class="aui bb-list">
  <thead>
    <tr class="assistive">
      <th class="name">Filename</th>
    </tr>
  </thead>
  <tbody>
    [[#files]]
    <tr class="iterable-item">
      <td class="name [[#isDirectory]]directory[[/isDirectory]]">
        <span class="aui-icon aui-icon-small[[#isDirectory]] aui-iconfont-devtools-folder-closed[[/isDirectory]][[^isDirectory]] aui-iconfont-devtools-file[[/isDirectory]]"></span>
        <a href="/mmorse1217/mth437/src/[[node]]/[[name]][[#branch]][[#isDirectory]]/[[/isDirectory]]?at=[[branch]][[/branch]]"
           title="[[name]]" class="execute" tabindex="-1">
          [[&highlightedName]]
        </a>
      </td>
    </tr>
    [[/files]]
  </tbody>
</table>

</script>
</form>


    </div>
  </div>

  <footer id="footer" role="contentinfo">
    <section class="footer-body">
      
  <ul>
    <li>
      <a class="support-ga" target="_blank"
           data-support-gaq-page="Blog"
           href="http://blog.bitbucket.org">Blog</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
           data-support-gaq-page="Home"
           href="/support">Support</a>
    </li>
    <li>
      <a class="support-ga"
           data-support-gaq-page="PlansPricing"
           href="/plans">Plans &amp; pricing</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
           data-support-gaq-page="DocumentationHome"
           href="//confluence.atlassian.com/display/BITBUCKET">Documentation</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
           data-support-gaq-page="DocumentationAPI"
           href="//confluence.atlassian.com/x/IYBGDQ">API</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
           data-support-gaq-page="SiteStatus"
           href="http://status.bitbucket.org/">Server status</a>
    </li>
    <li>
      <a class="support-ga" id="meta-info"
           data-support-gaq-page="MetaInfo"
           href="#">Version info</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
           data-support-gaq-page="EndUserAgreement"
           href="//www.atlassian.com/end-user-agreement?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=footer">Terms of service</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
           data-support-gaq-page="PrivacyPolicy"
           href="//www.atlassian.com/company/privacy?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=footer">Privacy policy</a>
    </li>
  </ul>
  <div id="meta-info-content" style="display: none;">
    <ul>
      
        
          <li>English</li>
        
      
      <li>
        <a class="support-ga" target="_blank"
           data-support-gaq-page="GitDocumentation"
           href="http://git-scm.com/">Git 1.8.5.2</a>
      </li>
      <li>
        <a class="support-ga" target="_blank"
           data-support-gaq-page="HgDocumentation"
           href="http://mercurial.selenic.com/">Mercurial 2.2.2</a>
      </li>
      <li>
        <a class="support-ga" target="_blank"
           data-support-gaq-page="DjangoDocumentation"
           href="https://www.djangoproject.com/">Django 1.4.6</a>
      </li>
      <li>
        <a class="support-ga" target="_blank"
           data-support-gaq-page="PythonDocumentation"
           href="http://www.python.org/">Python 2.7.3</a>
      </li>
      <li>
        <a class="support-ga" target="_blank"
           data-support-gaq-page="DeployedVersion"
           href="#">01877d2c365c / ea3b2d752f06 @ app02</a>
      </li>
    </ul>
  </div>
  <ul class="atlassian-links">
    <li>
      <a id="atlassian-jira-link" target="_blank" title="Track everything – bugs, tasks, deadlines, code – and pull reports to stay informed."
         href="http://www.atlassian.com/software/jira?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">JIRA</a>
    </li>
    <li>
      <a id="atlassian-confluence-link" target="_blank" title="Content Creation, Collaboration & Knowledge Sharing for Teams."
         href="http://www.atlassian.com/software/confluence/overview/team-collaboration-software?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">Confluence</a>
    </li>
    <li>
      <a id="atlassian-bamboo-link" target="_blank" title="Continuous integration and deployment, release management."
         href="http://www.atlassian.com/software/bamboo/overview?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">Bamboo</a>
    </li>
    <li>
      <a id="atlassian-stash-link" target="_blank" title="Git repo management, behind your firewall and Enterprise-ready."
         href="http://www.atlassian.com/software/stash/overview?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">Stash</a>
    </li>
    <li>
      <a id="atlassian-sourcetree-link" target="_blank" title="A free Git and Mercurial desktop client for Mac or Windows."
         href="http://www.sourcetreeapp.com/?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">SourceTree</a>
    </li>
    <li>
      <a id="atlassian-hipchat-link" target="_blank" title="Group chat and IM built for teams."
         href="http://www.hipchat.com/?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">HipChat</a>
    </li>
  </ul>
  <div id="footer-logo">
    <a target="_blank" title="Bitbucket is developed by Atlassian in San Francisco."
       href="http://www.atlassian.com?utm_source=bitbucket&amp;utm_medium=logo&amp;utm_campaign=bitbucket_footer">Atlassian</a>
  </div>
  <script id="share-form-template" type="text/html">
  

<div class="error aui-message hidden">
  <span class="aui-icon icon-error"></span>
  <div class="message"></div>
</div>
<table class="widget bb-list aui">
  <thead>
  <tr class="assistive">
    <th class="user">User</th>
    <th class="role">Role</th>
    <th class="actions">Actions</th>
  </tr>
  </thead>
  <tbody>
  <tr class="form">
    <td colspan="3">
      <form>
        <input type="text" class="user-or-email text user-input"
               placeholder="Username or email address"
               [[#disabled]]disabled[[/disabled]]>
        <button type="submit" class="aui-button aui-style" disabled>Add</button>
      </form>
    </td>
  </tr>
  </tbody>
</table>

</script>
  <script id="share-detail-template" type="text/html">
  

[[#username]]
<td class="user
           [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]"
    [[#error]]data-error="[[error]]"[[/error]]>
  <div title="[[displayName]]">
    <a href="/[[username]]" class="user">
      <img class="avatar avatar16" src="[[avatar]]" />
      <span>[[displayName]]</span>
    </a>
  </div>
</td>
[[/username]]
[[^username]]
<td class="email
           [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]"
    [[#error]]data-error="[[error]]"[[/error]]>
  <div title="[[email]]">
    <span class="aui-icon aui-icon-small aui-iconfont-email"></span>
    [[email]]
  </div>
</td>
[[/username]]
<td class="role
           [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]">
  <div>
    [[#group]]
      [[#hasCustomGroups]]
        <select class="group [[#noGroupChoices]]hidden[[/noGroupChoices]]">
          [[#groups]]
            <option value="[[slug]]"
                    [[#isSelected]]selected[[/isSelected]]>
              [[name]]
            </option>
          [[/groups]]
        </select>
      [[/hasCustomGroups]]
      [[^hasCustomGroups]]
      <label>
        <input type="checkbox" class="admin"
               [[#isAdmin]]checked[[/isAdmin]]>
        Administrator
      </label>
      [[/hasCustomGroups]]
    [[/group]]
    [[^group]]
      <ul>
        <li class="permission aui-lozenge aui-lozenge-complete
                   [[^read]]aui-lozenge-subtle[[/read]]"
            data-permission="read">
          read
        </li>
        <li class="permission aui-lozenge aui-lozenge-complete
                   [[^write]]aui-lozenge-subtle[[/write]]"
            data-permission="write">
          write
        </li>
        <li class="permission aui-lozenge aui-lozenge-complete
                   [[^admin]]aui-lozenge-subtle[[/admin]]"
            data-permission="admin">
          admin
        </li>
      </ul>
    [[/group]]
  </div>
</td>
<td class="actions
           [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]">
  <div>
    <a href="#" class="delete">
      <span class="aui-icon aui-icon-small aui-iconfont-remove">Delete</span>
    </a>
  </div>
</td>

</script>
  <script id="share-team-template" type="text/html">
  

<div class="clearfix">
  <span class="team-avatar-container">
    <img src="[[avatar]]" alt="[[display_name]]" title="[[display_name]]" class="avatar avatar32" />
  </span>
  <span class="team-name-container">
    [[display_name]]
  </span>
</div>
<p class="helptext">
  
    Existing users are granted access to this team immediately.
    New users will be sent an invitation.
  
</p>
<div class="share-form"></div>

</script>
  

    </section>
  </footer>
</div>


  
  <script id="require-js"
          src="https://d3oaxc4q5k2d6q.cloudfront.net/m/ea3b2d752f06/amd/build/main.js"
          data-main="https://d3oaxc4q5k2d6q.cloudfront.net/m/ea3b2d752f06/amd/build/main"
          data-page-module="repo/index"></script>




<script>
  (function () {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
  }());
</script>


  

<script id="source-changeset" type="text/html">
  

<a href="/mmorse1217/mth437/src/[[raw_node]]/[[path]]?at=master"
   class="[[#selected]]highlight[[/selected]]"
   data-hash="[[node]]">
  [[#author.username]]
    <img class="avatar avatar16" src="[[author.avatar]]"/>
    <span class="author" title="[[raw_author]]">[[author.display_name]]</span>
  [[/author.username]]
  [[^author.username]]
    <img class="avatar avatar16" src="https://d3oaxc4q5k2d6q.cloudfront.net/m/ea3b2d752f06/img/default_avatar/16/user_blue.png"/>
    <span class="author unmapped" title="[[raw_author]]">[[author]]</span>
  [[/author.username]]
  <time datetime="[[utctimestamp]]" data-title="true">[[utctimestamp]]</time>
  <span class="message">[[message]]</span>
</a>

</script>
<script id="embed-template" type="text/html">
  

<form class="aui embed">
  <label for="embed-code">Embed this source in another page:</label>
  <input type="text" readonly="true" value="&lt;script src=&quot;[[url]]&quot;&gt;&lt;/script&gt;" id="embed-code">
</form>

</script>
<script id="edit-form-template" type="text/html">
  


<form class="edit-form aui"
      data-repository="[[owner]]/[[slug]]"
      data-destination-repository="[[destinationOwner]]/[[destinationSlug]]"
      data-local-id="[[localID]]"
      data-is-writer="[[#isWriter]]true[[/isWriter]][[^isWriter]]false[[/isWriter]]"
      data-has-push-access="[[#hasPushAccess]]true[[/hasPushAccess]][[^hasPushAccess]]false[[/hasPushAccess]]"
      data-is-pull-request="[[#isPullRequest]]true[[/isPullRequest]][[^isPullRequest]]false[[/isPullRequest]]"
      data-hash="[[hash]]"
      data-branch="[[branch]]"
      data-path="[[path]]"
      data-preview-url="/xhr/[[owner]]/[[slug]]/preview/[[hash]]/[[encodedPath]]"
      data-preview-error="We had trouble generating your preview."
      data-unsaved-changes-error="Your changes will be lost. Are you sure you want to leave?">
  <div class="toolbar clearfix">
    <div class="primary">
      <h2>
        
          Editing <strong>[[path]]</strong> on branch: <strong>[[branch]]</strong>
        
      </h2>
    </div>
    <div class="secondary">
      <div class="hunk-nav aui-buttons">
        <button class="prev-hunk-button aui-button aui-button aui-style"
              disabled="disabled" aria-disabled="true" title="previous change">&#x25B2;</button>
        <button class="next-hunk-button aui-button aui-button aui-style"
              disabled="disabled" aria-disabled="true" title="next change">&#x25BC;</button>
      </div>
    </div>
  </div>
  <div class="file-editor">
    <textarea id="id_source">[[content]]</textarea>
  </div>
  <div class="preview-pane"></div>
  <div class="toolbar footer-toolbar clearfix">
    <div class="primary">
      <div id="syntax-mode" class="field">
        <label for="id_syntax-mode">Syntax mode:</label>
        <select id="id_syntax-mode">
          [[#syntaxes]]
            <option value="[[#mime]][[mime]][[/mime]][[^mime]][[mode]][[/mime]]">[[label]]</option>
          [[/syntaxes]]
        </select>
      </div>
      <div id="indent-mode" class="field">
        <label for="id_indent-mode">Indent mode:</label>
        <select id="id_indent-mode">
          <option value="tabs">Tabs</option>
          <option value="spaces">Spaces</option>
        </select>
      </div>
      <div id="indent-size" class="field">
        <label for="id_indent-size">Indent size:</label>
        <select id="id_indent-size">
          <option value="2">2</option>
          <option value="4">4</option>
          <option value="8">8</option>
        </select>
      </div>
    </div>
    <div class="secondary">
      <button class="preview-button aui-button aui-style"
              disabled="disabled" aria-disabled="true"
              data-preview-label="View diff"
              data-edit-label="Edit file">View diff</button>
      <button class="save-button aui-button aui-button-primary aui-style"
              disabled="disabled" aria-disabled="true">Commit</button>
      <a class="cancel-link" href="#">Cancel</a>
    </div>
  </div>
</form>

</script>
<script id="commit-form-template" type="text/html">
  

<form class="aui commit-form"
      data-title="Commit changes"
      data-default-message="[[filename]] edited online with Bitbucket"
      data-fork-error="We had trouble creating your fork."
      data-commit-error="We had trouble committing your changes."
      data-pull-request-error="We had trouble creating your pull request."
      data-update-error="We had trouble updating your pull request."
      data-branch-conflict-error="A branch with that name already exists."
      data-forking-message="Forking repository"
      data-committing-message="Committing changes"
      data-merging-message="Branching and merging changes"
      data-creating-pr-message="Creating pull request"
      data-updating-pr-message="Updating pull request"
      data-cta-label="Commit"
      data-cancel-label="Cancel">
  <div class="aui-message error hidden">
    <span class="aui-icon icon-error"></span>
    <span class="message"></span>
  </div>
  [[^isWriter]]
    <div class="aui-message info">
      <span class="aui-icon icon-info"></span>
      <p class="title">
        
          You don't have write access to this repository.
        
      </p>
      <span class="message">
        
          We'll create a fork for your changes and submit a
          pull request back to this repository.
        
      </span>
    </div>
  [[/isWriter]]
  <div class="field-group">
    <label for="id_message">Commit message</label>
    <textarea id="id_message" class="textarea"></textarea>
  </div>
  [[^isPullRequest]]
    [[#isWriter]]
      <fieldset class="group">
        <div class="checkbox">
          [[#hasPushAccess]]
            <input id="id_create-pullrequest" class="checkbox" type="checkbox">
            <label for="id_create-pullrequest">Create a pull request for this change</label>
          [[/hasPushAccess]]
          [[^hasPushAccess]]
            <input id="id_create-pullrequest" class="checkbox" type="checkbox" checked="checked" aria-disabled="true" disabled="true">
            <label for="id_create-pullrequest" title="Branch restrictions do not allow you to update this branch.">Create a pull request for this change</label>
          [[/hasPushAccess]]

        </div>
      </fieldset>
      <div id="pr-fields">
        <div id="branch-name-group" class="field-group">
          <label for="id_branch-name">Branch name</label>
          <input type="text" id="id_branch-name" class="text">
        </div>
        <div id="reviewers-group" class="field-group"
              data-api-url="/mmorse1217/mth437/pull-request/xhr/reviewer/mmorse1217/mth437/:reviewer_name">
          <label for="participants">Reviewers</label>
          <select id="participants" name="reviewers" multiple></select>
          <div class="error"></div>
          
        </div>
      </div>
    [[/isWriter]]
  [[/isPullRequest]]
  <button type="submit" id="id_submit">Commit</button>
</form>

</script>
<script id="merge-message-template" type="text/html">
  Merged [[hash]] into [[branch]]

[[message]]

</script>
<script id="commit-merge-error-template" type="text/html">
  



  We had trouble merging your changes. We stored them on the <strong>[[branch]]</strong> branch, so feel free to
  <a href="/[[owner]]/[[slug]]/full-commit/[[hash]]/[[path]]?at=[[encodedBranch]]">view them</a> or
  <a href="#" class="create-pull-request-link">create a pull request</a>.


</script>



<div data-modules="components/mentions/index">
  <script id="mention-result" type="text/html">
  
<img class="avatar avatar24" src="[[avatar_url]]">
[[#display_name]]
  <span class="display-name">[[&display_name]]</span> <small class="username">[[&username]]</small>
[[/display_name]]
[[^display_name]]
  <span class="username">[[&username]]</span>
[[/display_name]]
[[#is_teammate]][[^is_team]]
  <span class="aui-lozenge aui-lozenge-complete aui-lozenge-subtle">teammate</span>
[[/is_team]][[/is_teammate]]

</script>
  <script id="mention-call-to-action" type="text/html">
  
[[^query]]
<li class="bb-typeahead-item">Begin typing to search for a user</li>
[[/query]]
[[#query]]
<li class="bb-typeahead-item">Continue typing to search for a user</li>
[[/query]]

</script>
  <script id="mention-no-results" type="text/html">
  
[[^searching]]
<li class="bb-typeahead-item">Found no matching users for <em>[[query]]</em>.</li>
[[/searching]]
[[#searching]]
<li class="bb-typeahead-item bb-typeahead-searching">Searching for <em>[[query]]</em>.</li>
[[/searching]]

</script>
  
</div>


  

<!--[if lt IE 9]><script src="https://d3oaxc4q5k2d6q.cloudfront.net/m/ea3b2d752f06/lib/aui/js/aui-ie.js"></script><![endif]-->
<script type="text/javascript">if(!NREUMQ.f){NREUMQ.f=function(){NREUMQ.push(["load",new Date().getTime()]);var e=document.createElement("script");e.type="text/javascript";e.src=(("http:"===document.location.protocol)?"http:":"https:")+"//"+"js-agent.newrelic.com/nr-100.js";document.body.appendChild(e);if(NREUMQ.a)NREUMQ.a();};NREUMQ.a=window.onload;window.onload=NREUMQ.f;};NREUMQ.push(["nrfj","beacon-2.newrelic.com","a2cef8c3d3","1841284","Z11RZxdWW0cEVkYLDV4XdUYLVEFdClsdAAtEWkZQDlJBGgRFQhFMQl1DXFcZQ10AQkFYBFlUVlEXWEJHAA==",0,164,new Date().getTime(),"","","","",""]);</script></body>
</html>
