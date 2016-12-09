; ModuleID = '../src/test2.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test2(i32 %value) #0 {
  %1 = alloca i32, align 4
  %local = alloca i32, align 4
  store i32 %value, i32* %1, align 4
  %2 = load i32, i32* %1, align 4
  store i32 %2, i32* %local, align 4
  %3 = load i32, i32* %local, align 4
  %4 = add nsw i32 %3, 291
  store i32 %4, i32* %local, align 4
  %5 = load i32, i32* %local, align 4
  %6 = add nsw i32 %5, 273
  store i32 %6, i32* %local, align 4
  %7 = load i32, i32* %local, align 4
  ret i32 %7
}

attributes #0 = { nounwind "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-features"="+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
