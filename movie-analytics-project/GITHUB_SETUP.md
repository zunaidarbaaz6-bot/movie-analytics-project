# 📋 GitHub Setup Guide

Follow these steps to push your Movie Analytics project to GitHub:

## Prerequisites
- Git installed on your system
- GitHub account created

## Step 1: Initialize Git Repository

```bash
cd movie-analytics-project
git init
```

## Step 2: Add Files to Git

```bash
git add .
git status  # Verify files are staged
```

## Step 3: Create Initial Commit

```bash
git commit -m "Initial commit: Movie Analytics Project"
```

## Step 4: Create Repository on GitHub

1. Go to [GitHub](https://github.com)
2. Click the "+" icon in the top right
3. Select "New repository"
4. Name it: `movie-analytics-project`
5. **Don't** initialize with README (we already have one)
6. Click "Create repository"

## Step 5: Connect Local to Remote

Copy the commands shown on GitHub (replace `yourusername` with your GitHub username):

```bash
git remote add origin https://github.com/yourusername/movie-analytics-project.git
git branch -M main
git push -u origin main
```

## Step 6: Verify Upload

Visit: `https://github.com/yourusername/movie-analytics-project`

Your project should now be live on GitHub! 🎉

## Optional: Add Repository Topics

On your GitHub repository page:
1. Click the gear icon next to "About"
2. Add topics: `data-analysis`, `python`, `pandas`, `data-visualization`, `movie-analytics`, `portfolio-project`
3. Save changes

## Future Updates

After making changes:

```bash
git add .
git commit -m "Description of changes"
git push
```

## Tips for an Impressive Portfolio

1. **Add Screenshots**: Include visualization images in your README
2. **Write Clear Insights**: Document your findings
3. **Keep It Updated**: Add new analyses or improvements
4. **Star the Repo**: Make it easier to find
5. **Pin It**: Pin this repo on your GitHub profile

## Troubleshooting

### Authentication Issues
If you get authentication errors, you'll need to set up a Personal Access Token:
1. GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token with `repo` scope
3. Use the token as your password when pushing

### Large Files
If your dataset is too large (>100MB):
1. Add it to `.gitignore`
2. Provide instructions for users to generate or download it
3. Consider using Git LFS for large files

---

**Need help?** Check [GitHub's official documentation](https://docs.github.com)
