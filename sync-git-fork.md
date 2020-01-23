I have a fork of a git repository, and I want to pull in the latest updates from the canonical (upstream) repository.

My username is 'user'

I am working on a fork of a repository called 'repo', and my fork is in git at `git@git.server.example.com:user/repo.git`

The upstream of 'repo' is `git@git.server.example.com:upstreamuser/repo.git` (owned by uptreamuser)
```
user@user-pc ~
$ cd repo

user@user-pc ~/repo (master)
$ git remote add upstream git@git.server.example.com:upstreamuser/repo.git

user@user-pc ~/repo (master)
$ git fetch upstream
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 1), reused 0 (delta 0)
Unpacking objects: 100% (4/4), 2.48 KiB | 195.00 KiB/s, done.
From git.server.example.com:upstreamuser/repo
 * [new branch]      master     -> upstream/master

user@user-pc ~/repo (master)
$ git merge upstream/master
Updating c36e026..1e4358b
Fast-forward
 README.md | 12 ++++++++++++
 1 file changed, 12 insertions(+)

user@user-pc ~/repo (master)
$ git push origin master
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 859 bytes | 859.00 KiB/s, done.
Total 4 (delta 3), reused 0 (delta 0)
To git.server.example.com:user/repo.git
   c36e026..1e4358b  master -> master

user@user-pc ~/repo (master)
$
```
