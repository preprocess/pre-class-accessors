--DESCRIPTION--

Test class accessors fallback macros

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

    public function getName()
    {
        return $this->name;
    }

    public function __get($property)
    {
        if ($result·2 = $this->handleGetClassAccessors($property)) {
            return $result·2;
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
        if ($result·4 = $this->handleSetClassAccessors($property, $value)) {
            return $result·4;
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
        if ($result·6 = $this->handleUnsetClassAccessors($property)) {
            return $result·6;
        }

        print "unsetting {$property}";
    }
}
