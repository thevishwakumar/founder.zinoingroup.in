# PRODUCTION ROLLBACK STANDARD OPERATING PROCEDURE (SOP)

**Target Domain:** [founder.zinoingroup.in](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Lead Roles:** DevOps Engineer & Release Manager  
**Date:** November 14, 2026  
**Document Version:** 2.0.0 (Production Release SOP)  
**Document Purpose:** Rapid, zero-downtime recovery protocol in the event of an unforeseen production incident.

---

## 1. Rollback Trigger Criteria

A rollback should be initiated immediately if any of the following conditions occur post-deployment:
1. **HTTP 5xx Server Errors** or Cloudflare 520–524 origin timeout error screens.
2. **Critical Layout Breakdown** rendering content unreadable on mobile or desktop devices.
3. **Form Failure:** Submissions failing to reach the Web3Forms endpoint or throwing blocking script errors.
4. **Owner Request:** Immediate reversion requested by Vishwa K.

---

## 2. Production Backup Inventory

The following verified backups are stored locally in the project workspace:

| Backup File Name | Size | Date Created | Description / Scope |
|---|:---:|:---:|---|
| **`founder_zinoingroup_backup_step29_predeploy.zip`** | **3.51 MB** | Nov 14, 2026 | Full snapshot of v2.4.0 release candidate (HTML, WebP assets, JSON schemas, scripts). |
| **`live_production_snapshot.html`** | **73.59 KB** | Nov 14, 2026 | Exact capture of the currently running live production website at `https://founder.zinoingroup.in/`. |
| **`founder_zinoingroup_backup_final_step16.zip`** | **1.70 MB** | Nov 13, 2026 | Stable working baseline from Step 16. |
| **`founder_zinoingroup_backup_predeploy.zip`** | **1.68 MB** | Nov 13, 2026 | Historical pre-deployment backup. |

---

## 3. Rollback Procedures (Ranked by Speed)

### Method 1: Cloudflare Pages 1-Click Instant Rollback (< 30 Seconds)
*Best for: Cloudflare Pages continuous deployment.*
1. Log into the [Cloudflare Dashboard](https://dash.cloudflare.com/).
2. Navigate to **Workers & Pages** ➔ Select project **`founder-zinoingroup`**.
3. Under **Deployments**, locate the previous successful deployment.
4. Click the three dots (`...`) next to that deployment and select **Rollback to this deployment**.
5. Confirm the action.  
   *Result: Cloudflare's Anycast edge instantly switches 100% of global traffic back to the previous deployment artifact with zero build time.*

---

### Method 2: Git Revert Rollback (< 2 Minutes)
*Best for: Git repository connected to continuous deployment.*
```bash
# 1. Inspect recent commit history
git log -n 5 --oneline

# 2. Revert the latest deployment commit
git revert HEAD --no-edit

# 3. Push to master/main to trigger automatic redeployment
git push origin master
```

---

### Method 3: Zip Archive Restoration (< 3 Minutes)
*Best for: Manual SFTP / cPanel / Origin server hosting.*
1. Extract `founder_zinoingroup_backup_final_step16.zip` (or `founder_zinoingroup_backup_step29_predeploy.zip`).
2. Overwrite the web root (`public_html/` or `/var/www/html/`) with the extracted files.
3. Purge Cloudflare Edge cache:
   - Go to **Cloudflare Dashboard** ➔ Select `zinoingroup.in`.
   - Navigate to **Caching** ➔ **Configuration** ➔ Click **Purge Everything**.
4. Confirm resolution at `https://founder.zinoingroup.in/`.

---

### Method 4: Emergency Single-File HTML Restore (< 1 Minute)
*Best for: Instant recovery of the exact pre-Step-29 live page.*
1. Rename `live_production_snapshot.html` to `index.html`.
2. Upload `index.html` directly to the web root.
3. Purge Cloudflare Edge cache.
4. The live site will immediately revert to the exact pre-Step-29 baseline.

---

## 4. Post-Rollback Health Check

Following any rollback execution, run the following verification steps:
1. Verify HTTP status returns `200 OK` on `https://founder.zinoingroup.in/`.
2. Open Chrome DevTools (`F12`), check **Console** for 0 uncaught errors.
3. Verify that the hero section, navigation links, and theme toggle operate cleanly.
4. Send a test contact inquiry to verify form submission.
5. Notify the owner that the rollback has completed successfully.
