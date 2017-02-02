--DESCRIPTION--

Test accessor fallbacks

--GIVEN--

namespace Pre\ClassAccessors\Fixture;

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

--EXPECT--

namespace Pre\ClassAccessors\Fixture;

class Fixture
{
    use \Pre\ClassAccessors\ClassAccessorsTrait;

    private $name;

    private function getName()
    {
        return $this->name;
    }

    public function __get($property)
    {
        $this->handleGetClassAccessors($property);

        print "getting {$property}";
    }

    private $age;

    private function setAge($value)
    {
        $this->age = $value;
    }

    public function __set($property, $value)
    {
        $this->handleSetClassAccessors($property, $value);

        print "setting {$property}";
    }

    private $feature;

    private function unsetFeature()
    {
        $this->feature = null;
    }

    public function __unset($property)
    {
        $this->handleUnsetClassAccessors($property);

        print "unsetting {$property}";
    }
}
