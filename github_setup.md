# GitHub Repository Setup Instructions

## Add Your Remote Repository

Replace YOUR_GITHUB_USERNAME and YOUR_REPOSITORY_NAME in the following command:

```powershell
cd "c:\Users\ulhiltner\Arbeit\ProjektePublikationen\paper8_ReviewPaperWriting_DSS4ES\subgroup4_data\1_LiteratureSearch\initial_screening_all_downloads\literature_toolkit_publication"
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
```

For example, if your GitHub username is "uhiltner" and your repository name is "universal-lit-screening", the command would be:

```powershell
cd "c:\Users\ulhiltner\Arbeit\ProjektePublikationen\paper8_ReviewPaperWriting_DSS4ES\subgroup4_data\1_LiteratureSearch\initial_screening_all_downloads\literature_toolkit_publication"
git remote add origin https://github.com/uhiltner/universal-lit-screening.git
```

## Push Your Code to GitHub

After adding the remote, push your code:

```powershell
git push -u origin main
```

You'll be prompted to enter your GitHub credentials. You might need to use a personal access token instead of your password if you have two-factor authentication enabled.

## Creating a Release (Optional)

After pushing your code, you can create a release:

1. Go to your GitHub repository in the browser
2. Click on "Releases" on the right sidebar
3. Click "Create a new release"
4. Set the tag version to "v2.0"
5. Title it "Universal Literature Screening Toolkit v2.0"
6. Add release notes describing key features
7. Click "Publish release"

## Connect to Zenodo for DOI (Optional)

If you want a DOI for your software:

1. Go to https://zenodo.org/
2. Log in with your GitHub account
3. Enable the repository in Zenodo settings
4. Create a release on GitHub (steps above)
5. Zenodo will automatically create a DOI for your repository
