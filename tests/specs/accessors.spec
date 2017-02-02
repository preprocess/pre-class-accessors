--DESCRIPTION--

Test accessors

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

    private function setName($value)
    {
        $this->name = ucwords($value);
    }

    private function unsetName()
    {
        $this->name = "unset";
    }

    private $person_age;

    private function setPersonAge($value)
    {
        $this->person_age = round($value);
    }
}
