# OneMoar

use any code, just please give a little credit.

peace pooks. ✌️

NOTICE: Other addons depend on Kodi/Player global setting "Play next video automatically" for PlayNext.  Having this always on has unintended consequences and/or may conflict with this and other addons.  The other addons should be encouraged to move away from this dependency by "copying," developing their own process, or reverting to the original Venom process.

- maybe MOAR to come...
- Significantly simplified the playlist creation for PlayNext.
- Removed `checkPlayNextEpisodes` from use.
- Fixed `checkPlayNextEpisodes` function to not overwrite user settings other than "Episodes."  Moved to `service.py` because this has to set before clicking on listitem for Kodi to load complete directory into playlist.
- Significant changes.
- Rewrite colorpicker/custom dialogs...  Questioning why I am doing this.
- Refactor/rewrite scrape/resolve dialogs.
- Exorcise the demons (legacy artwork).
- Rewrite of "Icon Only/Hidden" progress dialog.
- Tweak for colorpicker to avoid carrying 527 png images with addon.  Bless whoever organized the color array values.
- Enable "Developer mode" to change the background.  Return to the settings category and select "Defaults" to clear it if needed.
- "Prefer TMDB artwork" setting now includes TMDB logo art, which is only slightly faster than Fanart.tv.
- "Flatten TV seasons" setting now includes "One Season", when only one season available episodes will list without season list.
- removed metadatahandler dependency, added Dradis watchedcache for local movie/episode watched tracking.
- file pruning: favorites.db, thumbs.db...
- removed beautifulsoup dependency, didn't see import anywhere.
- merged nexus/matrix versions as seems to be no difference in the addon code.
- other fixes/changes.
