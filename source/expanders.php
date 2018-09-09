<?php

namespace Pre\ClassAccessors;

use Yay\Engine;
use Yay\TokenStream;

function classAccessorsReturn(TokenStream $stream, Engine $engine): TokenStream
{
    if (!empty($stream->current())) {
        $stream = ": {$stream}";
    }

    return TokenStream::fromSource(
        $engine->expand($stream, "", Engine::GC_ENGINE_DISABLED)
    );
}
