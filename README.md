A set of common used functions/classes I end up using in my projects.

Automatically document all methods in the `pyutils` package using:

````bash
rg --glob "*.py" -N "^def " pyutils | sort | \
 awk -F: '
{
file=$1
line=$0
sub(/^[^:]+:/, "", line)
sub(/^ *def /, "", line)
if (file != last_file) {
if (last_file != "") print "```"
      print "\n" file "\n```python"
last_file=file
}
print line
}
END { print "```" }' >> README.md
````

# Methods

pyutils/dicts/utils.py

```python
camel_to_snake_dict(camel_dict: dict[str, Any]) -> dict[str, Any]:
clean_dict(d: dict[Any, Any]) -> dict[Any, Any]:
copy_dict(d: dict[str, Any], exclude: list[str] | None = None) -> dict[str, Any]:
```

pyutils/lists/utils.py

```python
flatten(xs: Iterable[Any]) -> Iterator[Any]:
```

pyutils/paths/utils.py

```python
create_temp_dir() -> tempfile.TemporaryDirectory[str]:
remove_temp_dir(temp_dir: tempfile.TemporaryDirectory[Any] | str) -> None:
```

pyutils/shortcuts/checks.py

```python
all_none(*args: object | None) -> bool:
all_not_none(*args: object | None) -> bool:
all_or_none(*args: object | None) -> bool:
none(g: Generator[Any, Any, Any]) -> bool:
only_one_not_none(*args: object | None) -> bool:
```

pyutils/shortcuts/dates.py

```python
date_range(start_date: date, end_date: date) -> list[date]:
week_range_from_date(d: datetime | date) -> tuple[date, date]:
weeks_between(d1: datetime | date, d2: datetime | date) -> timedelta:
week_to_date(week: int, year: int) -> datetime:
```

pyutils/shortcuts/utils.py

```python
generate_unique_code(length: int = 8) -> str:
random_user_agent() -> str:
```

pyutils/strings/cleanup.py

```python
lstrip_conjunctions(text: str) -> str:
remove_brackets(text: str, preserve_content: bool = False) -> str:
remove_conjunctions(text: str) -> str:
remove_genders(text: str) -> str:
remove_hyphens(word: str) -> str:
remove_leading_hyphen(word: str) -> str:
remove_parenthesis(text: str, preserve_content: bool = False) -> str:
remove_roman(text: str) -> str:
remove_symbols(text: str, preserve_quotes: bool = False) -> str:
remove_trailing_hyphen(word: str) -> str:
unaccent(text: str) -> str:
whitespaces_clean(text: str) -> str:
```

pyutils/strings/datetime.py

```python
find_date(maybe_date_str: str, day_first: bool | None = None) -> date | None:
find_time(maybe_time_str: str) -> time | None:
```

pyutils/strings/integer.py

```python
int_or_none(v: str) -> int | None:
```

pyutils/strings/lemma.py

```python
expand_lemmas(lemmas: list[str], expansions: list[list[str | None]]) -> list[list[str]]:
normalize_synonyms(phrase: str, synonyms: dict[str, list[str]]) -> str:
```

pyutils/strings/money.py

```python
split_money(value: str) -> tuple[str | None, float | None]:
symbol_to_currency(symbol: str) -> str | None:
```

pyutils/strings/normalize.py

```python
apply_replaces(text: str, normalizations: dict[str, list[str]]) -> str:
match_normalization(text: str, normalization_rules: dict[str, list[list[str]]]) -> str:
```

pyutils/strings/roman.py

```python
find_roman(word: str) -> str | None:
int_to_roman(num: int) -> str:
roman_to_int(s: str) -> int:
```

pyutils/strings/similarity.py

```python
closest_result(keyword: str, elements: list[str]) -> tuple[str | None, float]:
levenshtein_distance(s1: str, s2: str) -> float:
```

pyutils/strings/transformers.py

```python
camel_to_snake(camel_str: str) -> str:
int_to_european(number: int, grouping: bool = False) -> str:
```

pyutils/validators/bank.py

```python
is_valid_bic(bic: str) -> bool:
is_valid_iban(iban: str) -> bool:
```

pyutils/validators/dni.py

```python
is_valid_dni(dni: str) -> bool:
```

pyutils/validators/email.py

```python
is_valid_email(email: str) -> bool:
```

pyutils/validators/figi.py

```python
is_valid_figi(figi: str) -> bool:
```

pyutils/validators/isin.py

```python
is_valid_isin(isin: str) -> bool:
```

pyutils/validators/url.py

```python
is_valid_url(url: str) -> bool:
```
