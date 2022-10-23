# TransitNU API

API for subway services in Boston.

## API Endpoints

/api/v1/train

- Data for all trains running currently
- Returns:
  [{'id': ..., 'line': {...}, 'location': {...}, 'status': ..., 'stop': ..., 'occupancy': ..., 'speed': ..., 'last_update': ...}, ...]

/api/v1/<train_id>

- Data for a specific train
- Returns: {'id': ..., 'line': {...}, 'location': {...}, 'status': ..., 'stop': ..., 'occupancy': ..., 'speed': ..., 'last_update': ...}

/api/v1/train/line/<line_id>

- Data for all trains on a line
- returns: [{'id': ..., 'line': {'id': <line_id>, ...}, 'location': {...}, 'status': ..., 'stop': ..., 'occupancy': ..., 'speed': ..., 'last_update': ...}, ...]

/api/v1/stop

- Data for all stops
- returns: [{'id': ..., 'name': ..., 'location': ..., 'municipality': ..., 'street': ...}, ...]

/api/v1/stop/<stop_id>

- Data for a specific stop
- returns: {'id': ..., 'name': ..., 'location': ..., 'municipality': ..., 'street': ...}

/api/v1/line

- Data for all lines
- returns: [{'id': ..., 'name': ..., 'color': ..., 'direction_destinations': [..., ...], 'direction_names': [..., ...], 'line': ..., 'polylines': [...]}, ...]

/api/v1/line/<line_id>

- Data for a specific line
- returns: {'id': ..., 'name': ..., 'color': ..., 'direction_destinations': [..., ...], 'direction_names': [..., ...], 'line': ..., 'polylines': [...]}

## More to come

...

## License

[MIT](https://choosealicense.com/licenses/mit/)
