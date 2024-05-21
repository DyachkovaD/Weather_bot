from token_data import OPENW_TOKEN


async def city_lat_lon(session, city):
    async with session.get(
            url=f'http://api.openweathermap.org/geo/1.0/direct?q={city}'
                f'&limit=1&appid={OPENW_TOKEN}',
    ) as resp:
        data = await resp.json()

        lat = data[0]['lat']
        lon = data[0]['lon']
        return lat, lon

async def collect_forecast(session, lat, lon):
   async with session.get(
           url=f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}'
               f'&appid={OPENW_TOKEN}',
   ) as resp:
       data = await resp.json()
       return data
