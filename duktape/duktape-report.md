###### Duktape version:

```
Checked revision: {{version|trim}}
```

###### OS:

```
{{platform}}
```

###### Test case:

```javascript
{% if reduced %}
{{reduced}}
{% else %}
{{test}}
{% endif %}
```

###### Backtrace:

```text
{{stderr|trim}}
{{backtrace|trim}}
```

###### Build script:

```bash
{{build_command|trim}}
```

###### duktape-fuzzinator-options.yaml:

```yaml
{{build_config|trim}}
```

<sup>Found by [Fuzzinator](http://fuzzinator.readthedocs.io/) with {{fuzzer}}. </sup>
