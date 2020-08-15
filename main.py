import xbmcemu

kodi = xbmcemu.KodiInstance("/home/marius/.kodi")
#result = kodi.run_addon("plugin.video.needforponies", "action=list_season")
result = kodi.run_url("plugin://plugin.video.needforponies/?action=play_episode&season_id=season-3&episode_id=episode-13")
result.pretty_print()
print(result)
