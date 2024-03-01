source: [https://github.com/mrgsi/tmdbh.players](https://github.com/mrgsi/tmdbh.players)

`pov.autoplay.json`
```
{
    "name" : "POV Auto Play",
    "plugin" : "plugin.video.pov",
    "priority" : 500,
    "is_resolvable": "true",
    "play_movie" : "plugin://plugin.video.pov/?mode=play_media&media_type=movie&query={name}&year={year}&poster={poster}&title={title}&tmdb_id={id}",
    "play_episode" : "plugin://plugin.video.pov/?mode=play_media&media_type=episode&query={showname}&year={year}&season={season}&episode={episode}&ep_name={title}&tmdb_id={tmdb}&premiered={firstaired}"
}
```
`pov.select.json`
```
{
    "name": "POV Source Select",
    "plugin": "plugin.video.pov",
    "priority": 500,
    "is_resolvable": "false",
    "play_movie": "plugin://plugin.video.pov/?mode=play_media&media_type=movie&query={name}&year={year}&poster={poster}&title={title}&tmdb_id={id}&autoplay=false",
    "play_episode": "plugin://plugin.video.pov/?mode=play_media&media_type=episode&query={showname}&year={year}&season={season}&episode={episode}&ep_name={title}&tmdb_id={tmdb}&premiered={firstaired}&autoplay=false"
}
```
`dradis.autoplay.json`
```
{
    "name" : "Dradis Auto Play", 
    "plugin" : "plugin.video.dradis", 
    "priority" : 100, 
    "is_resolvable" : "true", 
    "play_episode" : "plugin://plugin.video.dradis/?action=play&title={title_url}&year={showyear}&imdb={imdb}&tmdb={tmdb}&tvdb={tvdb}&season={season}&episode={episode}&tvshowtitle={showname_url}&premiered={firstaired}select=1", 
    "play_movie" : "plugin://plugin.video.dradis/?action=play&title={title_url}&year={year}&imdb={imdb}&tmdb={tmdb}&select=1"
}
```
`dradis.select.json`
```
{
    "name" : "Dradis Source Select", 
    "plugin" : "plugin.video.dradis", 
    "priority" : 101, 
    "is_resolvable" : "true", 
    "play_episode" : "plugin://plugin.video.dradis/?action=play&title={title_url}&year={showyear}&imdb={imdb}&tmdb={tmdb}&tvdb={tvdb}&season={season}&episode={episode}&tvshowtitle={showname_url}&premiered={firstaired}&meta=%7B%22rating%22%3A+%22%22%2C+%22code%22%3A+%22{imdb}%22%2C+%22tmdb%22%3A+{tmdb}%2C+%22imdb%22%3A+%22{imdb}%22%2C+%22year%22%3A+%22{showyear}%22%2C+%22duration%22%3A+%22%22%2C+%22plot%22%3A+%22{plot_escaped}%22%2C+%22votes%22%3A+%22%22%2C+%22thumb%22%3A+%22{thumbnail}%22%2C+%22title%22%3A+%22{title_url}%22%2C+%22tvdb%22%3A+%22{tvdb}%22%2C+%22label%22%3A+%22{title_url}%22%2C+%22season%22%3A+%22{season}%22%2C+%22status%22%3A+%22%22%2C+%22poster%22%3A+%22{poster}%22%2C+%22tvshowtitle%22%3A+%22{showname_url}%22%2C+%22mediatype%22%3A+%22episode%22%2C+%22episode%22%3A+%22{episode}%22%2C+%22studio%22%3A+%22%22%2C+%22genre%22%3A+%22%22%2C+%22banner%22%3A+%22{thumbnail}%22%2C+%22premiered%22%3A+%22{firstaired}%22%2C+%22fanart%22%3A+%22{fanart}%22%7D&select=0", 
    "play_movie" : "plugin://plugin.video.dradis/?action=play&title={title_url}&year={year}&imdb={imdb}&tmdb={tmdb}&meta=%7B%22rating%22%3A+%22%22%2C+%22code%22%3A+%22{imdb}%22%2C+%22tmdb%22%3A+%22{id}%22%2C+%22imdb%22%3A+%22{imdb}%22%2C+%22year%22%3A+%22{year}%22%2C+%22duration%22%3A+%22%22%2C+%22plot%22%3A+%22{plot_escaped}%22%2C+%22votes%22%3A+%22%22%2C+%22title%22%3A+%22{title_url}%22%2C+%22fanart%22%3A+%22{fanart}%22%2C+%22tagline%22%3A+%22%22%2C+%22writer%22%3A+%22%22%2C+%22next%22%3A+%22%22%2C+%22poster%22%3A+%22{poster}%22%2C+%22mediatype%22%3A+%22movie%22%2C+%22director%22%3A+%22%22%2C+%22studio%22%3A+%22%22%2C+%22genre%22%3A+%22%22%2C+%22metacache%22%3A+true%2C+%22premiered%22%3A+%22{premiered}%22%2C+%22originaltitle%22%3A+%22{title_url}%22%2C+%22cast%22%3A+%5B%22{actors}%22%5D%2C+%22mpaa%22%3A+%22%22%7D&select=0"
}
```
