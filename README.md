# `ccal`

**Usage**:

```console
$ ccal [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--confirm / --no-confirm`: Confirm action
* `--help`: Show this message and exit.

**Commands**:

* `add`: Add your event to google calendar
* `delete`: description delete delete func
* `gui`: Run server Web view for calendar
* `list`: Query events from Google calendar
* `login`: description login func
* `logout`: description logout func
* `update`: description update func

## `ccal add`

Add your event to google calendar

**Usage**:

```console
$ ccal add [OPTIONS] EVENT [DATE]:[%Y-%m-%d]
```

**Arguments**:

* `EVENT`: Enter event name  [required]
* `[DATE]:[%Y-%m-%d]`: Enter event date  [default: 2021-11-03]

**Options**:

* `-d, --detail TEXT`: Enter event details
* `-p, --place TEXT`: Enter event details
* `--help`: Show this message and exit.

## `ccal delete`

description delete delete func

**Usage**:

```console
$ ccal delete [OPTIONS] ID
```

**Arguments**:

* `ID`: Enter Event's ID  [required]

**Options**:

* `--help`: Show this message and exit.

## `ccal gui`

Run server Web view for calendar

**Usage**:

```console
$ ccal gui [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `ccal list`

Query events from Google calendar

**Usage**:

```console
$ ccal list [OPTIONS]
```

**Options**:

* `--on-month INTEGER`: Query events on month[1-12] and current year[2021]
* `--date-start [%Y-%m-%d]`: Query events start from this date  [default: 2021-11-01]
* `--date-end [%Y-%m-%d]`: Query events end to this date  [default: 2021-12-01]
* `-v, --view`: List event then select to see detail
* `--help`: Show this message and exit.

## `ccal login`

description login func

**Usage**:

```console
$ ccal login [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `ccal logout`

description logout func

**Usage**:

```console
$ ccal logout [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `ccal update`

description update func

**Usage**:

```console
$ ccal update [OPTIONS] [ID]
```

**Arguments**:

* `[ID]`: Enter ID of event referance

**Options**:

* `-e, --event TEXT`: Enter new event's name
* `-p, --place TEXT`: Enter new event's location
* `-d, --detail TEXT`: Enter new event's detail
* `--help`: Show this message and exit.
