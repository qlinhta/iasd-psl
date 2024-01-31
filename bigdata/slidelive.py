from myslideslive import SlidesLive

msl = SlidesLive(
    'https://slideslive.com/embed/presentation/39004359?js_embed_version=3&embed_init_token=eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MDM0MDA0NDMsImV4cCI6MTcwMzUzMDA0MywidSI6eyJ1dWlkIjoiZDQ4NGRkYzYtOTZiOS00ZjcxLTk0ZTMtZGZjOTA2MDVkYjgzIiwiaSI6bnVsbCwiZSI6bnVsbCwibSI6ZmFsc2V9LCJkIjoiaWNtbC5jYyJ9.ADg5cfrbm4NXvD7rasbd_p_HKM_mWgA37OgfFvGbUkM&embed_parent_url=https%3A%2F%2Ficml.cc%2Fvirtual%2F2023%2Ftutorial%2F21559&embed_origin=https%3A%2F%2Ficml.cc&embed_container_id=presentation-embed-39004359&auto_load=true&auto_play=false&zoom_ratio=&disable_fullscreen=false&locale=en&vertical_enabled=true&vertical_enabled_on_mobile=false&allow_hidden_controls_when_paused=true&fit_to_viewport=true&custom_user_id=&user_uuid=d484ddc6-96b9-4f71-94e3-dfc90605db83')
msl.download_slides(slide=(1074, 1075))
msl.compose_video()
