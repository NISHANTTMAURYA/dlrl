# Document: Git-Scm Com Book En V2 Getting-Started-Abo E76F7Ee4

---

[![Git](/images/logo@2x.png)](/)

![](/images/dark-mode.svg)
    * [Trademark](/about/trademark)
  * [Learn](/learn)
    * [Book](/book)
    * [Cheat Sheet](/cheat-sheet)
    * [Videos](/videos)
    * [External Links](/doc/ext)
  * [Tools](/tools)
    * [Command Line](/tools/command-line)
    * [GUIs](/tools/guis)
    * [Hosting](/tools/hosting)
  * [Reference](/docs)
  * [Install](/install)
  * [Community](/community)

* * *

This book is available in [English](/book/en/v2/Getting-Started-About-Version-Control). 

Full translation available in  [azərbaycan dili](/book/az/v2/Ba%c5%9flan%c4%9f%c4%b1c-Versiyaya-N%c9%99zar%c9%99t-Haqq%c4%b1nda),  
---  
[български език](/book/bg/v2/%d0%9d%d0%b0%d1%87%d0%b0%d0%bb%d0%be-%d0%97%d0%b0-Version-Control-%d1%81%d0%b8%d1%81%d1%82%d0%b5%d0%bc%d0%b8%d1%82%d0%b5),  
[Deutsch](/book/de/v2/Erste-Schritte-Was-ist-Versionsverwaltung?),  
[Español](/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Acerca-del-Control-de-Versiones),  
[فارسی](/book/fa/v2/%d8%b4%d8%b1%d9%88%d8%b9-%d8%a8%d9%87-%da%a9%d8%a7%d8%b1-getting-started-%d8%af%d8%b1%d8%a8%d8%a7%d8%b1%d9%87-%d9%88%d8%b1%da%98%d9%86-%da%a9%d9%86%d8%aa%d8%b1%d9%84-About-Version-Control),  
[Français](/book/fr/v2/D%c3%a9marrage-rapide-%c3%80-propos-de-la-gestion-de-version),  
[Ελληνικά](/book/gr/v2/%ce%9e%ce%b5%ce%ba%ce%b9%ce%bd%cf%8e%ce%bd%cf%84%ce%b1%cf%82-%ce%bc%ce%b5-%cf%84%ce%bf-Git-%ce%a3%cf%87%ce%b5%cf%84%ce%b9%ce%ba%ce%ac-%ce%bc%ce%b5-%cf%84%ce%bf%ce%bd-%ce%ad%ce%bb%ce%b5%ce%b3%cf%87%ce%bf-%ce%b5%ce%ba%ce%b4%cf%8c%cf%83%ce%b5%cf%89%ce%bd),  
[日本語](/book/ja/v2/%e4%bd%bf%e3%81%84%e5%a7%8b%e3%82%81%e3%82%8b-%e3%83%90%e3%83%bc%e3%82%b8%e3%83%a7%e3%83%b3%e7%ae%a1%e7%90%86%e3%81%ab%e9%96%a2%e3%81%97%e3%81%a6),  
[한국어](/book/ko/v2/%ec%8b%9c%ec%9e%91%ed%95%98%ea%b8%b0-%eb%b2%84%ec%a0%84-%ea%b4%80%eb%a6%ac%eb%9e%80?),  
[Nederlands](/book/nl/v2/Aan-de-slag-Over-versiebeheer),  
[Русский](/book/ru/v2/%d0%92%d0%b2%d0%b5%d0%b4%d0%b5%d0%bd%d0%b8%d0%b5-%d0%9e-%d1%81%d0%b8%d1%81%d1%82%d0%b5%d0%bc%d0%b5-%d0%ba%d0%be%d0%bd%d1%82%d1%80%d0%be%d0%bb%d1%8f-%d0%b2%d0%b5%d1%80%d1%81%d0%b8%d0%b9),  
[Slovenščina](/book/sl/v2/Za%c4%8detek-O-nadzoru-razli%c4%8dic),  
[Tagalog](/book/tl/v2/Pagsisimula-Tungkol-sa-Bersyon-Kontrol),  
[Українська](/book/uk/v2/%d0%92%d1%81%d1%82%d1%83%d0%bf-%d0%9f%d1%80%d0%be-%d1%81%d0%b8%d1%81%d1%82%d0%b5%d0%bc%d1%83-%d0%ba%d0%be%d0%bd%d1%82%d1%80%d0%be%d0%bb%d1%8e-%d0%b2%d0%b5%d1%80%d1%81%d1%96%d0%b9),  
[简体中文](/book/zh/v2/%e8%b5%b7%e6%ad%a5-%e5%85%b3%e4%ba%8e%e7%89%88%e6%9c%ac%e6%8e%a7%e5%88%b6),  
  
Partial translations available in  [Čeština](/book/cs/v2/%c3%9avod-Spr%c3%a1va-verz%c3%ad),  
---  
[Македонски](/book/mk/v2/%d0%9f%d0%be%d1%87%d0%b5%d1%82%d0%be%d0%ba-%d0%97%d0%b0-%d0%b2%d0%b5%d1%80%d0%b7%d0%b8%d1%81%d0%ba%d0%b0-%d0%ba%d0%be%d0%bd%d1%82%d1%80%d0%be%d0%bb%d0%b0),  
[Polski](/book/pl/v2/Pierwsze-kroki-Wprowadzenie-do-kontroli-wersji),  
[Српски](/book/sr/v2/%d0%9f%d0%be%d1%87%d0%b5%d1%82%d0%b0%d0%ba-%d0%9e-%d0%ba%d0%be%d0%bd%d1%82%d1%80%d0%be%d0%bb%d0%b8-%d0%b2%d0%b5%d1%80%d0%b7%d0%b8%d1%98%d0%b5),  
[Ўзбекча](/book/uz/v2/%d0%98%d1%88-%d0%b1%d0%be%d1%88%d0%bb%d0%b0%d0%bd%d0%b8%d1%88%d0%b8-%d0%a2%d0%b0%d0%bb%d2%9b%d0%b8%d0%bd%d0%bb%d0%b0%d1%80%d0%bd%d0%b8-%d0%b1%d0%be%d1%88%d2%9b%d0%b0%d1%80%d0%b8%d1%88-%d2%b3%d0%b0%d2%9b%d0%b8%d0%b4%d0%b0),  
[繁體中文](/book/zh-tw/v2/%e9%96%8b%e5%a7%8b-%e9%97%9c%e6%96%bc%e7%89%88%e6%9c%ac%e6%8e%a7%e5%88%b6),  
  
Translations started for  [Беларуская](/book/be/v2/%d0%9f%d0%b5%d1%80%d1%88%d1%8b%d1%8f-%d0%ba%d1%80%d0%be%d0%ba%d1%96-About-Version-Control),  
---  
[Indonesian](/book/id/v2/Memulai-Tentang-Version-Control),  
[Italiano](/book/it/v2/Per-Iniziare-Il-Controllo-di-Versione),  
[Bahasa Melayu](/book/ms/v2/Getting-Started-About-Version-Control),  
[Português (Brasil)](/book/pt-br/v2/Come%c3%a7ando-Sobre-Controle-de-Vers%c3%a3o),  
[Português (Portugal)](/book/pt-pt/v2/Come%c3%a7ando-Sobre-Controle-de-Vers%c3%a3o),  
[Svenska](/book/sv/v2/Kom-ig%c3%a5ng-Om-versionshantering),  
[Türkçe](/book/tr/v2/Ba%c5%9flang%c4%b1%c3%a7-S%c3%bcr%c3%bcm-Denetimi).  
  
* * *

The source of this book is [hosted on GitHub.](https://github.com/progit/progit2) Patches, suggestions and comments are welcome. 

[Chapters ▾](#)

  1. ## 1\. [Getting Started](/book/en/v2/Getting-Started-About-Version-Control)

     1. 1.1 [About Version Control](/book/en/v2/Getting-Started-About-Version-Control)
     2. 1.2 [A Short History of Git](/book/en/v2/Getting-Started-A-Short-History-of-Git)
     3. 1.3 [What is Git?](/book/en/v2/Getting-Started-What-is-Git%3F)
     4. 1.4 [The Command Line](/book/en/v2/Getting-Started-The-Command-Line)
     5. 1.5 [Installing Git](/book/en/v2/Getting-Started-Installing-Git)
     6. 1.6 [First-Time Git Setup](/book/en/v2/Getting-Started-First-Time-Git-Setup)
     7. 1.7 [Getting Help](/book/en/v2/Getting-Started-Getting-Help)
     8. 1.8 [Summary](/book/en/v2/Getting-Started-Summary)
  2. ## 2\. [Git Basics](/book/en/v2/Git-Basics-Getting-a-Git-Repository)

     1. 2.1 [Getting a Git Repository](/book/en/v2/Git-Basics-Getting-a-Git-Repository)
     2. 2.2 [Recording Changes to the Repository](/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
     3. 2.3 [Viewing the Commit History](/book/en/v2/Git-Basics-Viewing-the-Commit-History)
     4. 2.4 [Undoing Things](/book/en/v2/Git-Basics-Undoing-Things)
     5. 2.5 [Working with Remotes](/book/en/v2/Git-Basics-Working-with-Remotes)
     6. 2.6 [Tagging](/book/en/v2/Git-Basics-Tagging)
     7. 2.7 [Git Aliases](/book/en/v2/Git-Basics-Git-Aliases)
     8. 2.8 [Summary](/book/en/v2/Git-Basics-Summary)
  3. ## 3\. [Git Branching](/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

     1. 3.1 [Branches in a Nutshell](/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
     2. 3.2 [Basic Branching and Merging](/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
     3. 3.3 [Branch Management](/book/en/v2/Git-Branching-Branch-Management)
     4. 3.4 [Branching Workflows](/book/en/v2/Git-Branching-Branching-Workflows)
     5. 3.5 [Remote Branches](/book/en/v2/Git-Branching-Remote-Branches)
     6. 3.6 [Rebasing](/book/en/v2/Git-Branching-Rebasing)
     7. 3.7 [Summary](/book/en/v2/Git-Branching-Summary)
  4. ## 4\. [Git on the Server](/book/en/v2/Git-on-the-Server-The-Protocols)

     1. 4.1 [The Protocols](/book/en/v2/Git-on-the-Server-The-Protocols)
     2. 4.2 [Getting Git on a Server](/book/en/v2/Git-on-the-Server-Getting-Git-on-a-Server)
     3. 4.3 [Generating Your SSH Public Key](/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key)
     4. 4.4 [Setting Up the Server](/book/en/v2/Git-on-the-Server-Setting-Up-the-Server)
     5. 4.5 [Git Daemon](/book/en/v2/Git-on-the-Server-Git-Daemon)
     6. 4.6 [Smart HTTP](/book/en/v2/Git-on-the-Server-Smart-HTTP)
     7. 4.7 [GitWeb](/book/en/v2/Git-on-the-Server-GitWeb)
     8. 4.8 [GitLab](/book/en/v2/Git-on-the-Server-GitLab)
     9. 4.9 [Third Party Hosted Options](/book/en/v2/Git-on-the-Server-Third-Party-Hosted-Options)
     10. 4.10 [Summary](/book/en/v2/Git-on-the-Server-Summary)
  5. ## 5\. [Distributed Git](/book/en/v2/Distributed-Git-Distributed-Workflows)

     1. 5.1 [Distributed Workflows](/book/en/v2/Distributed-Git-Distributed-Workflows)
     2. 5.2 [Contributing to a Project](/book/en/v2/Distributed-Git-Contributing-to-a-Project)
     3. 5.3 [Maintaining a Project](/book/en/v2/Distributed-Git-Maintaining-a-Project)
     4. 5.4 [Summary](/book/en/v2/Distributed-Git-Summary)

  1. ## 6\. [GitHub](/book/en/v2/GitHub-Account-Setup-and-Configuration)

     1. 6.1 [Account Setup and Configuration](/book/en/v2/GitHub-Account-Setup-and-Configuration)
     2. 6.2 [Contributing to a Project](/book/en/v2/GitHub-Contributing-to-a-Project)
     3. 6.3 [Maintaining a Project](/book/en/v2/GitHub-Maintaining-a-Project)
     4. 6.4 [Managing an organization](/book/en/v2/GitHub-Managing-an-organization)
     5. 6.5 [Scripting GitHub](/book/en/v2/GitHub-Scripting-GitHub)
     6. 6.6 [Summary](/book/en/v2/GitHub-Summary)
  2. ## 7\. [Git Tools](/book/en/v2/Git-Tools-Revision-Selection)

     1. 7.1 [Revision Selection](/book/en/v2/Git-Tools-Revision-Selection)
     2. 7.2 [Interactive Staging](/book/en/v2/Git-Tools-Interactive-Staging)
     3. 7.3 [Stashing and Cleaning](/book/en/v2/Git-Tools-Stashing-and-Cleaning)
     4. 7.4 [Signing Your Work](/book/en/v2/Git-Tools-Signing-Your-Work)
     5. 7.5 [Searching](/book/en/v2/Git-Tools-Searching)
     6. 7.6 [Rewriting History](/book/en/v2/Git-Tools-Rewriting-History)
     7. 7.7 [Reset Demystified](/book/en/v2/Git-Tools-Reset-Demystified)
     8. 7.8 [Advanced Merging](/book/en/v2/Git-Tools-Advanced-Merging)
     9. 7.9 [Rerere](/book/en/v2/Git-Tools-Rerere)
     10. 7.10 [Debugging with Git](/book/en/v2/Git-Tools-Debugging-with-Git)
     11. 7.11 [Submodules](/book/en/v2/Git-Tools-Submodules)
     12. 7.12 [Bundling](/book/en/v2/Git-Tools-Bundling)
     13. 7.13 [Replace](/book/en/v2/Git-Tools-Replace)
     14. 7.14 [Credential Storage](/book/en/v2/Git-Tools-Credential-Storage)
     15. 7.15 [Summary](/book/en/v2/Git-Tools-Summary)
  3. ## 8\. [Customizing Git](/book/en/v2/Customizing-Git-Git-Configuration)

     1. 8.1 [Git Configuration](/book/en/v2/Customizing-Git-Git-Configuration)
     2. 8.2 [Git Attributes](/book/en/v2/Customizing-Git-Git-Attributes)
     3. 8.3 [Git Hooks](/book/en/v2/Customizing-Git-Git-Hooks)
     4. 8.4 [An Example Git-Enforced Policy](/book/en/v2/Customizing-Git-An-Example-Git-Enforced-Policy)
     5. 8.5 [Summary](/book/en/v2/Customizing-Git-Summary)
  4. ## 9\. [Git and Other Systems](/book/en/v2/Git-and-Other-Systems-Git-as-a-Client)

     1. 9.1 [Git as a Client](/book/en/v2/Git-and-Other-Systems-Git-as-a-Client)
     2. 9.2 [Migrating to Git](/book/en/v2/Git-and-Other-Systems-Migrating-to-Git)
     3. 9.3 [Summary](/book/en/v2/Git-and-Other-Systems-Summary)
  5. ## 10\. [Git Internals](/book/en/v2/Git-Internals-Plumbing-and-Porcelain)

     1. 10.1 [Plumbing and Porcelain](/book/en/v2/Git-Internals-Plumbing-and-Porcelain)
     2. 10.2 [Git Objects](/book/en/v2/Git-Internals-Git-Objects)
     3. 10.3 [Git References](/book/en/v2/Git-Internals-Git-References)
     4. 10.4 [Packfiles](/book/en/v2/Git-Internals-Packfiles)
     5. 10.5 [The Refspec](/book/en/v2/Git-Internals-The-Refspec)
     6. 10.6 [Transfer Protocols](/book/en/v2/Git-Internals-Transfer-Protocols)
     7. 10.7 [Maintenance and Data Recovery](/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery)
     8. 10.8 [Environment Variables](/book/en/v2/Git-Internals-Environment-Variables)
     9. 10.9 [Summary](/book/en/v2/Git-Internals-Summary)

  1. ## A1. [Appendix A: Git in Other Environments](/book/en/v2/Appendix-A:-Git-in-Other-Environments-Graphical-Interfaces)

     1. A1.1 [Graphical Interfaces](/book/en/v2/Appendix-A:-Git-in-Other-Environments-Graphical-Interfaces)
     2. A1.2 [Git in Visual Studio](/book/en/v2/Appendix-A:-Git-in-Other-Environments-Git-in-Visual-Studio)
     3. A1.3 [Git in Visual Studio Code](/book/en/v2/Appendix-A:-Git-in-Other-Environments-Git-in-Visual-Studio-Code)
     4. A1.4 [Git in IntelliJ / PyCharm / WebStorm / PhpStorm / RubyMine](/book/en/v2/Appendix-A:-Git-in-Other-Environments-Git-in-IntelliJ-/-PyCharm-/-WebStorm-/-PhpStorm-/-RubyMine)
     5. A1.5 [Git in Sublime Text](/book/en/v2/Appendix-A:-Git-in-Other-Environments-Git-in-Sublime-Text)
     6. A1.6 [Git in Bash](/book/en/v2/Appendix-A:-Git-in-Other-Environments-Git-in-Bash)
     7. A1.7 [Git in Zsh](/book/en/v2/Appendix-A:-Git-in-Other-Environments-Git-in-Zsh)
     8. A1.8 [Git in PowerShell](/book/en/v2/Appendix-A:-Git-in-Other-Environments-Git-in-PowerShell)
     9. A1.9 [Summary](/book/en/v2/Appendix-A:-Git-in-Other-Environments-Summary)
  2. ## A2. [Appendix B: Embedding Git in your Applications](/book/en/v2/Appendix-B:-Embedding-Git-in-your-Applications-Command-line-Git)

     1. A2.1 [Command-line Git](/book/en/v2/Appendix-B:-Embedding-Git-in-your-Applications-Command-line-Git)
     2. A2.2 [Libgit2](/book/en/v2/Appendix-B:-Embedding-Git-in-your-Applications-Libgit2)
     3. A2.3 [JGit](/book/en/v2/Appendix-B:-Embedding-Git-in-your-Applications-JGit)
     4. A2.4 [go-git](/book/en/v2/Appendix-B:-Embedding-Git-in-your-Applications-go-git)
     5. A2.5 [Dulwich](/book/en/v2/Appendix-B:-Embedding-Git-in-your-Applications-Dulwich)
  3. ## A3. [Appendix C: Git Commands](/book/en/v2/Appendix-C:-Git-Commands-Setup-and-Config)

     1. A3.1 [Setup and Config](/book/en/v2/Appendix-C:-Git-Commands-Setup-and-Config)
     2. A3.2 [Getting and Creating Projects](/book/en/v2/Appendix-C:-Git-Commands-Getting-and-Creating-Projects)
     3. A3.3 [Basic Snapshotting](/book/en/v2/Appendix-C:-Git-Commands-Basic-Snapshotting)
     4. A3.4 [Branching and Merging](/book/en/v2/Appendix-C:-Git-Commands-Branching-and-Merging)
     5. A3.5 [Sharing and Updating Projects](/book/en/v2/Appendix-C:-Git-Commands-Sharing-and-Updating-Projects)
     6. A3.6 [Inspection and Comparison](/book/en/v2/Appendix-C:-Git-Commands-Inspection-and-Comparison)
     7. A3.7 [Debugging](/book/en/v2/Appendix-C:-Git-Commands-Debugging)
     8. A3.8 [Patching](/book/en/v2/Appendix-C:-Git-Commands-Patching)
     9. A3.9 [Email](/book/en/v2/Appendix-C:-Git-Commands-Email)
     10. A3.10 [External Systems](/book/en/v2/Appendix-C:-Git-Commands-External-Systems)
     11. A3.11 [Administration](/book/en/v2/Appendix-C:-Git-Commands-Administration)
     12. A3.12 [Plumbing Commands](/book/en/v2/Appendix-C:-Git-Commands-Plumbing-Commands)

2nd Edition 

# 1.1 Getting Started - About Version Control

This chapter will be about getting started with Git. We will begin by explaining some background on version control tools, then move on to how to get Git running on your system and finally how to get it set up to start working with. At the end of this chapter you should understand why Git is around, why you should use it and you should be all set up to do so.

## About Version Control

What is “version control”, and why should you care? Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. For the examples in this book, you will use software source code as the files being version controlled, though in reality you can do this with nearly any type of file on a computer.

If you are a graphic or web designer and want to keep every version of an image or layout (which you would most certainly want to), a Version Control System (VCS) is a very wise thing to use. It allows you to revert selected files back to a previous state, revert the entire project back to a previous state, compare changes over time, see who last modified something that might be causing a problem, who introduced an issue and when, and more. Using a VCS also generally means that if you screw things up or lose files, you can easily recover. In addition, you get all this for very little overhead.

### Local Version Control Systems

Many people’s version-control method of choice is to copy files into another directory (perhaps a time-stamped directory, if they’re clever). This approach is very common because it is so simple, but it is also incredibly error prone. It is easy to forget which directory you’re in and accidentally write to the wrong file or copy over files you don’t mean to.

To deal with this issue, programmers long ago developed local VCSs that had a simple database that kept all the changes to files under revision control.

![Local version control diagram](/book/en/v2/images/local.png)

Figure 1. Local version control diagram

One of the most popular VCS tools was a system called RCS, which is still distributed with many computers today. [RCS](https://www.gnu.org/software/rcs/) works by keeping patch sets (that is, the differences between files) in a special format on disk; it can then re-create what any file looked like at any point in time by adding up all the patches.

### Centralized Version Control Systems

The next major issue that people encounter is that they need to collaborate with developers on other systems. To deal with this problem, Centralized Version Control Systems (CVCSs) were developed. These systems (such as CVS, Subversion, and Perforce) have a single server that contains all the versioned files, and a number of clients that check out files from that central place. For many years, this has been the standard for version control.

![Centralized version control diagram](/book/en/v2/images/centralized.png)

Figure 2. Centralized version control diagram

This setup offers many advantages, especially over local VCSs. For example, everyone knows to a certain degree what everyone else on the project is doing. Administrators have fine-grained control over who can do what, and it’s far easier to administer a CVCS than it is to deal with local databases on every client.

However, this setup also has some serious downsides. The most obvious is the single point of failure that the centralized server represents. If that server goes down for an hour, then during that hour nobody can collaborate at all or save versioned changes to anything they’re working on. If the hard disk the central database is on becomes corrupted, and proper backups haven’t been kept, you lose absolutely everything — the entire history of the project except whatever single snapshots people happen to have on their local machines. Local VCSs suffer from this same problem — whenever you have the entire history of the project in a single place, you risk losing everything.

### Distributed Version Control Systems

This is where Distributed Version Control Systems (DVCSs) step in. In a DVCS (such as Git, Mercurial or Darcs), clients don’t just check out the latest snapshot of the files; rather, they fully mirror the repository, including its full history. Thus, if any server dies, and these systems were collaborating via that server, any of the client repositories can be copied back up to the server to restore it. Every clone is really a full backup of all the data.

![Distributed version control diagram](/book/en/v2/images/distributed.png)

Figure 3. Distributed version control diagram

Furthermore, many of these systems deal pretty well with having several remote repositories they can work with, so you can collaborate with different groups of people in different ways simultaneously within the same project. This allows you to set up several types of workflows that aren’t possible in centralized systems, such as hierarchical models.

[prev](/book/en/v2/Getting-Started-About-Version-Control) | [next](/book/en/v2/Getting-Started-A-Short-History-of-Git)

[About this site](/site)  
Patches, suggestions, and comments are welcome. 

Git is a member of [Software Freedom Conservancy](/sfc)