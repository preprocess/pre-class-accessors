<?php

namespace Pre\ClassAccessors;

use PHPUnit\Framework\TestCase;

class MacroTest extends TestCase
{
    public function testClassAccessors()
    {
        $fixture = new Fixture\Fixture();

        $this->assertEmpty($fixture->name);

        $fixture->name = "the fixture";

        $this->assertEquals("The Fixture", $fixture->name);

        unset($fixture->name);

        $this->assertEquals("unset", $fixture->name);
    }

    public function testFallback()
    {
        $fixture = new Fixture\Fixture();

        $this->assertEquals("fallback", $fixture->foo);
    }
}
