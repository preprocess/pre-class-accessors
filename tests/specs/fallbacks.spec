class Fixture
{
    private $name {
        get {
            return $this->name;
        }
    }

    public function __get($property)
    {
        accessors;

        print "getting {$property}";
    }

    private $age {
        set {
            $this->age = $value;
        }
    }

    public function __set($property, $value)
    {
        accessors;

        print "setting {$property}";
    }

    private $feature {
        unset {
            $this->feature = null;
        }
    }

    public function __unset($property)
    {
        accessors;

        print "unsetting {$property}";
    }
}

~~~

class Fixture
{
    use \Pre\ClassAccessors\ClassAccessorsTrait;

    private $name;

    public function getName()
    {
        return $this->name;
    }

    public function __get($property)
    {
        if ($result = $this->handleGetClassAccessors($property)) {
            return $result;
        }

        print "getting {$property}";
    }

    private $age;

    public function setAge($value)
    {
        $this->age = $value;
    }

    public function __set($property, $value)
    {
        if ($result = $this->handleSetClassAccessors($property, $value)) {
            return $result;
        }

        print "setting {$property}";
    }

    private $feature;

    public function unsetFeature()
    {
        $this->feature = null;
    }

    public function __unset($property)
    {
        if ($result = $this->handleUnsetClassAccessors($property)) {
            return $result;
        }

        print "unsetting {$property}";
    }
}
