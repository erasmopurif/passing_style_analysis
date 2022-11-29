# Passing Style Analyser - Serie A 2021/22

Final thesis for the [2nd course on Football Data Intelligence](https://www.sics.it/corso-football-data-intelligence/) organized by [SICS](https://www.sics.it/en/) and [Soccerment](https://soccerment.com/).

### Author: Erasmo Purificato
---

With this application, you can analyze the passing style of each Serie A 2021/22 team.

The two pages available in the sidebar are described below.

## Full Pitch & Field Tilt Networks

After selected a **single matchday** or a **range of matchdays**, it is possible to analyze:
* a single team,
* two teams, or
* all the 20 Serie A teams,
by viewing their **passing network** in the **most used formation** for the selected matchdays, either visualizing the **full-pitch** or **field-tilt** passing network.

Additionally, the user can select the number of minimum passes to be displayed in the passing networks (Note that for multiple matchdays, this value is multiplied by the number of selected matchdays).

## Match Status Networks

After selected a **single matchday** or a **range of matchdays**, and a **team**, it is possible to analyze the full-pitch passing network for each **match status** (i.e. winning, drawing, losing) and view their barycenter in the "passing" scenario.

Additionally, the user can decide whether or not to keep the goalkeeper in the barycenter computation, and select the number of minimum passes to be displayed in the passing networks (Note that in this case, for multiple matchdays, this value is **NOT** multiplied by the number of selected matchdays).
