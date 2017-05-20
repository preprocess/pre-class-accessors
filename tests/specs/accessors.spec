--DESCRIPTION--

Test class accessors macros

--GIVEN--

namespace Pre\ClassAccessors\Fixture;

class Fixture
{
    private $name {
        get {
            return $this->name;
        }

        set {
            $this->name = ucwords($value);
        }

        unset {
            $this->name = "unset";
        }
    };

    private $person_age {
        set {
            $this->person_age = round($value);
        }
    };

    private bool $shouldDoThing {
        get {
            return $this->shouldDoThing;
        }

        set {
            $this->shouldDoThing = $value;
        }
    }

    private string $typed {
        get {
            return $this->typed;
        }

        set {
            $this->typed = $value;
        }
    }

    protected $protected {
        get {
            return $this->protected;
        }
    }

    private $simple {
        get; set; unset;
    }

    private $immutable {
        immutable set {
            $this->immutable = $value;
        }

        immutable unset {
            unset($this->immutable);
        }
    }

    private $immutableSimple {
        immutable set;
        immutable unset;
    }
}

--EXPECT--

namespace Pre\ClassAccessors\Fixture;

class Fixture
{
    use \Pre\ClassAccessors\ClassAccessorsTrait;

    private $name;

    public function getName()
    {
        return $this->name;
    }

    public function setName($value)
    {
        $this->name = ucwords($value);
    }

    public function unsetName()
    {
        $this->name = "unset";
    }

    private $person_age;

    public function setPersonAge($value)
    {
        $this->person_age = round($value);
    }

    private $shouldDoThing;

    public function getShouldDoThing(): bool
    {
        return $this->shouldDoThing;
    }

    public function setShouldDoThing(bool $value)
    {
        $this->shouldDoThing = $value;
    }

    private $typed;

    public function getTyped(): string
    {
        return $this->typed;
    }

    public function setTyped(string $value)
    {
        $this->typed = $value;
    }

    protected $protected;

    public function getProtected()
    {
        return $this->protected;
    }

    private $simple;

    public function getSimple()
    {
        return $this->simple;
    }

    public function setSimple($value)
    {
        $this->simple = $value;
        return $this;
    }

    public function unsetSimple()
    {
        unset($this->simple);
        return $this;
    }

    private $immutable;

    public function withImmutable($value)
    {
        $clone = clone $this;

        $bound = \Closure::bind(function () use ($value) {
            $this->immutable = $value;
        }, $clone);

        $bound();

        return $clone;
    }

    public function withoutImmutable($value)
    {
        $clone = clone $this;

        $bound = \Closure::bind(function () use ($value) {
            unset($this->immutable);
        }, $clone);

        $bound();

        return $clone;
    }

    private $immutableSimple;

    public function withImmutableSimple($value)
    {
        $clone = clone($this);
        $clone->immutableSimple = $value;
        return $clone;
    }

    public function withoutImmutableSimple($value)
    {
        $clone = clone($this);
        unset($clone->immutableSimple);
        return $clone;
    }
}
