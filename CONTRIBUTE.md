# Contributors guide

## Setup your own forked repository

This is a one-time process.

1) Fork the original repository (https://github.com/UNICT-DMI/Telegram-DMIFAQ-Bot) with the 'Fork' button on the upper right. This will create a copy of this repository on your profile.

2) Clone your fork locally. I suggest you to connect via an [SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) from now on: 
```
git clone git@github.com:*YOURNICKNAME*/Telegram-DMIFAQ-Bot.git
```

4) Add the original repository as a remote. This will help you pull updates easily when you start working on a new contribution: 
```
git remote add upstream git@github.com:UNICT-DMI/Telegram-DMIFAQ-Bot.git
```

## Work on the code

These steps should be repeated each time you work on a new contribution to the code.

1) Pull updates from the main repository. ***It is important to do this every time before you start coding on your local copy***: 
```
git checkout master
git pull upstream master
```

2) Create a new local branch, name it significally in respect to the feature you are introducing.
```
git checkout -b new-feature
```

3) Code, commit, push whatever you want on your fork (origin).

***Never push on your own master, this will make integration and sudden pull of updates a lot more difficult***.

***Never push on upstream, it shouldn't be allowed by the repository itself but be careful anyway***.

4) Create a pull request between your 'my-feature' branch on UNICT-DMI. If the pipeline fails for any reason, check the output and correct any issue. Once the pipeline stops complaining your code will be reviewed by the maintainers and merged once ready. Thanks!
