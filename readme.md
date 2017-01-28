# Pre Class Accessors

This adds class accessor macros, to allow C#-style getters, setters, and unsetters to PHP classes.

## Using

The first step is to require this repository in your plugin repository:

```
composer require pre/short-closures
```

Then, you can add getters, setters, and unsetters; using the following syntax:

```php
class Sprocket
{
    private $type {
        get {
            return $this->type;
        }

        set {
            $this->type = $value;
        }

        unset {
            $this->type = "type has been unset";
        }
    }
}
```

These will be connected through `__get`, `__set`, and `__unset` methods, defined in the `Pre\AccessorsTrait`. If you override these magic methods, these accessors will not work. You can use `__get_fallback`, `__set_fallback`, and `__unset_fallback` if you'd like to add your own magic method functionality.

## Testing

There are a few tests, to make sure the class accessors are correctly compiled, and that the fallback methods work as intended. You can run these tests with:

```
vendor/bin/phpunit
```

This assumes you've cloned this repository and run `composer install` beforehand.

## Versioning

This library follows [Semver](http://semver.org). According to Semver, you will be able to upgrade to any minor or patch version of this library without any breaking changes to the public API. Semver also requires that we clearly define the public API for this library.

All methods, with `public` visibility, are part of the public API. All other methods are not part of the public API. Where possible, we'll try to keep `protected` methods backwards-compatible in minor/patch versions, but if you're overriding methods then please test your work before upgrading.
