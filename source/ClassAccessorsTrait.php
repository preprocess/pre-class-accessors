<?php

namespace Pre\ClassAccessors;

trait ClassAccessorsTrait
{
    /**
     * @inheritdoc
     *
     * @param string $property
     * @param mixed $value
     */
    public function __get($property)
    {
        return $this->handleGetClassAccessors($property);
    }

    /**
     * Finds and invokes getters.
     *
     * @param string $property
     * @param mixed $value
     */
    protected function handleGetClassAccessors($property)
    {
        $property = $this->studly($property);

        if (method_exists($this, "get{$property}")) {
            return $this->{"get{$property}"}();
        }
    }

    /**
     * Replaces "this_format" and "this-format" with "ThisFormat".
     *
     * @return string
     */
    private function studly($string)
    {
        return str_replace(" ", "", ucwords(str_replace(["-", "_"], " ", $string)));
    }

    /**
     * @inheritdoc
     *
     * @param string $property
     * @param mixed $value
     */
    public function __set($property, $value)
    {
        return $this->handleSetClassAccessors($property, $value);
    }

    /**
     * Finds and invokes setters.
     *
     * @param string $property
     * @param mixed $value
     */
    protected function handleSetClassAccessors($property, $value)
    {
        $property = $this->studly($property);

        if (method_exists($this, "set{$property}")) {
            return $this->{"set{$property}"}($value);
        }
    }

    /**
     * @inheritdoc
     *
     * @param string $property
     */
    public function __unset($property)
    {
        return $this->handleUnsetClassAccessors($property);
    }

    /**
     * Finds and invokes unsetters.
     *
     * @param string $property
     */
    protected function handleUnsetClassAccessors($property)
    {
        $property = $this->studly($property);

        if (method_exists($this, "unset{$property}")) {
            return $this->{"unset{$property}"}();
        }
    }
}
