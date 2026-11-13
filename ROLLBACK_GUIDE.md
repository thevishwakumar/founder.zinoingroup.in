# PRODUCTION ROLLBACK STANDARD OPERATING PROCEDURE (SOP)

**Target Domain:** https://founder.zinoingroup.in/  
**Website Owner:** Vishwa K  
**Lead Roles:** DevOps Engineer & Release Manager  
**Date:** November 2026  
**Document Purpose:** Rapid, zero-downtime recovery protocol in the event of an unforeseen production incident.

---

## 1. Rollback Trigger Criteria

A rollback should be initiated immediately if any of the following conditions occur post-deployment:
1. **HTTP 5xx Server Errors** or Cloudflare 520–524 origin timeout error screens.
2. **Critical Layout Breakdown** rendering content unreadable on mobile or desktop devices.
3. **Form Failure:** Submissions failing to reach the Web3Forms endpoint.
4. **Owner Request:** Immediate reversion requested by Vishwa K.

---

## 2. Rollback Methods (Ranked by Speed)

### Method 1: Cloudflare Pages 1-Click Instant Rollback (< 30 Seconds)
If hosting on Cloudflare Pages:
1. Log into the [Cloudflare Dashboard](https://dash.cloudflare.com/).
2. Navigate to **Workers & Pages** ➔ Select project **`founder-zinoingroup`**.
3. Under **Deployments**, locate the previous successful deployment.
4. Click the three dots (`...`) next to that deployment and select **Rollback to this deployment**.
5. Confirm the action.  
   *Result: Cloudflare's Anycast edge instantly switches 100% of global traffic back to the previous deployment artifact with zero build time.*

---

### Method 2: Git Checkpoint Rollback (< 2 Minutes)
If continuous deployment is linked to GitHub:
```bash
# 1. Inspect recent commit history
git log -n 5 --oneline

# 2. Revert the latest deployment commit
git revert HEAD --no-edit

# 3. Push to master/main to trigger automatic redeployment
git push origin master
```
Alternatively, restore the working copy from the pre-implementation commit (`72b018a`):
```bash
git checkout 72b018a -- founder.zinoingroup.in/
git commit -m "revert: rollback founder website to commit 72b018a"
git push origin master
```

---

### Method 3: Local File Backup Restoration (< 1 Minute)
To restore directly from local physical backup files:

#### A. Restoring `index.html` from Pre-Step 14 Checkpoint:
```powershell
Copy-Item -Path "founder.zinoingroup.in\index.html.pre-step14" -Destination "founder.zinoingroup.in\index.html" -Force
```

#### B. Restoring from Master Pre-Deploy ZIP Archive:
The master safety archive `founder_zinoingroup_backup_predeploy.zip` (1.68 MB) contains the complete original website state:
```powershell
Expand-Archive -Path "founder_zinoingroup_backup_predeploy.zip" -DestinationPath "founder.zinoingroup.in_restored" -Force
```

---

## 3. Mandatory Post-Rollback Edge Cache Purge

After executing any rollback method, purge the Cloudflare Edge Cache so visitors receive the reverted files immediately:

1. In the **Cloudflare Dashboard**, navigate to **Caching** ➔ **Configuration**.
2. Click **Purge Everything**.
3. In Chrome, open an incognito window or perform a hard refresh (`Ctrl + Shift + R` or `Cmd + Shift + R`) at:  
   `https://founder.zinoingroup.in/`

---

## 4. Post-Rollback Verification Checklist

- [ ] HTTP response status returns **200 OK**.
- [ ] Page renders without visual glitch or missing images.
- [ ] Console contains **0 unhandled JavaScript errors**.
- [ ] Navigation anchor scrolling functions properly.
- [ ] Contact form loads correctly.
- [ ] Incident logged with root cause documented.
